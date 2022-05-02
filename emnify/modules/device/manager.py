import typing
import emnify.modules.device.api_call_manager as device_call_managers
from emnify.errors import UnexpectedArgumentException
from emnify.modules.device.models import Device, GetDeviceFilterSet, QFilterDeviceListQueryParam, DeviceEvent, \
    DeviceStatus, TariffProfile, ServiceProfile, ListSms, SmsCreateModel, RetrieveDevice, UpdateDevice, CreateDevice
from emnify import constants as emnify_constants
from emnify import errors as emnify_errors


class DeviceManager:
    """
    Manager that allows to get/retrieve/create/update/send_sms to device
    """
    def __init__(self, client):
        self.client = client

    @property
    def device_model(self):
        return Device

    @property
    def list_sms_model(self):
        return ListSms

    @property
    def device_detailed_model(self):
        return RetrieveDevice

    @property
    def sms_create_model(self):
        return SmsCreateModel

    @property
    def event_model(self):
        return DeviceEvent

    @property
    def status_model(self):
        return DeviceStatus

    @property
    def device_create_model(self):
        return CreateDevice

    @property
    def device_update_model(self):
        return UpdateDevice

    @property
    def service_profile_model(self):
        return ServiceProfile

    @property
    def tariff_profile_model(self):
        return TariffProfile

    @property
    def sort_device_param_enum(self):
        return emnify_constants.DeviceSortEnum

    @property
    def device_list_filterset_model(self):
        return GetDeviceFilterSet

    @property
    def get_device_q_filterset(self) -> typing.Type[QFilterDeviceListQueryParam]:
        return QFilterDeviceListQueryParam

    def get_device_sms_list(self, *args, device: typing.Union[Device, int]) -> ListSms:
        device_id = self.validate_device(device)
        sms_response = device_call_managers.GetEventsByDevice().call_api(
            client=self.client, path_params={'endpoint_id': device_id}
        )
        for sms in sms_response:
            yield ListSms(**sms)

    def send_sms(self, *args, device: typing.Union[Device, int, RetrieveDevice], sms: SmsCreateModel) -> bool:
        device_id = self.validate_device(device)
        if not isinstance(sms, SmsCreateModel):
            raise UnexpectedArgumentException('sms argument must be SmsCreateModel instance')
        return device_call_managers.SendSmsToDevice().call_api(
            client=self.client, path_params={'endpoint_id': device_id}, data=sms.dict(exclude_none=True)
        )

    def update_device(self, *args, device_id: int, device: UpdateDevice):
        return device_call_managers.UpdateDevice().call_api(
            client=self.client, data=device.dict(exclude_none=True), path_params={'endpoint_id': device_id}
        )

    def get_devices_list(self, *args, query_params: GetDeviceFilterSet = None, **kwargs):

        if query_params:
            query_params = self.transform_all_devices_filter_params(query_params)
        devices_response = device_call_managers.GetAllDevicesApiCall()\
            .call_api(client=self.client, query_params=query_params, *args, **kwargs)
        for device in devices_response:
            yield Device(**device)

    def get_device_events_list(self, device: typing.Union[Device, int]):
        """
        :param device: Device pydantic model or int
        :return: Generator with Device objects
        """
        device_id = self.validate_device(device)
        events_response = device_call_managers.GetEventsByDevice().call_api(
            client=self.client, path_params={'endpoint_id': device_id}
        )
        for event in events_response:
            yield DeviceEvent(**event)

    def change_status(
            self, device: typing.Union[UpdateDevice, Device, int],
            enable: bool = None, disable: bool = None
    ) -> None:
        """
        :param device: id or device model for update
        :param enable: boolean parameter for enable a Device
        :param disable: boolean parameter for enable a Device
        """
        if not (enable or disable) or (enable and disable):
            raise emnify_errors.ValidationErrorException('"enable" or "disable" arguments must be provided ')
        new_status = emnify_constants.DeviceStatuses.ENABLED_DICT.value \
            if enable else emnify_constants.DeviceStatuses.DISABLED_DICT.value
        if isinstance(device, int):
            device = self.retrieve_device(device)
        self.__check_device_status(device, new_status)
        action = 'enable' if enable else 'disable'
        return self.__change_device_status(action, device)

    def disable_device(self, device_id: int):
        """
        Method for changing a device status to 'disabled'
        """
        device_update = self.device_update_model(status=emnify_constants.DeviceStatuses.DISABLED_DICT.value)
        self.update_device(device=device_update, device_id=device_id)

    def release_sim(self, device_id: int):
        """
        this method allow to release the assigned SIM from device
        releasing sim sdk take 3 actions:
            - suspend the sim
            - disable the endpoint
            - release the sim
        """
        device = self.retrieve_device(device_id=device_id)
        if not device.sim:
            raise emnify_errors.ValidationErrorException('Device must have sim to release')
        self.client.sim.suspend_sim(sim_id=device.sim.id)
        self.disable_device(device_id=device.id)
        return device_call_managers.UpdateDevice().call_api(
            client=self.client, data={"sim": {"id": None}}, path_params={'endpoint_id': device_id}
        )

    def assign_sim(self, device_id: int, sim_id: int, enable: bool = False) -> None:
        """
        this method allow to assign a SIM to the device
        """
        device = self.retrieve_device(device_id=device_id)
        sim = self.client.sim.retrieve_sim(sim_id=sim_id)
        if enable:
            self.client.sim.activate_sim(sim_id=sim_id)
            self.change_status(device.id, enable=True)
        else:
            if sim.status.id == emnify_constants.SimStatuses.SUSPENDED_ID.value:
                self.change_status(device.id, disable=True)
            elif sim.status.id == emnify_constants.SimStatuses.ACTIVATED_ID.value:
                self.change_status(device.id, enable=True)

        self.update_device(device=self.device_update_model(sim={"id": sim.id}), device_id=device.id)

    def create_device(self, device: Device) -> bool:
        if not isinstance(device, self.device_model):
            raise UnexpectedArgumentException('Argument must contain filled Device model')
        return device_call_managers.CreateDevice().call_api(client=self.client, data=device.dict(exclude_none=True))

    def retrieve_device(self, device_id: int) -> RetrieveDevice:
        if not isinstance(device_id, int) or device_id <= 0:
            raise UnexpectedArgumentException('Device id must be positive integer')
        response = device_call_managers.RetrieveDevice().call_api(
            client=self.client, path_params={'endpoint_id': device_id}
        )
        return RetrieveDevice(**response)

    @staticmethod
    def validate_device(device: Device) -> int:
        if isinstance(device, Device) or isinstance(device, RetrieveDevice):
            return device.id
        elif isinstance(device, int):
            return device
        else:
            raise UnexpectedArgumentException('device must be Device instance or int')

    @staticmethod
    def __check_device_status(device, status: dict):
        """
        Hidden method for checking device for status update
        devices to activate must have activated sim
        """
        if status == emnify_constants.SimStatuses.ACTIVATED_DICT:
            if not device.sim:
                raise emnify_errors.ValidationErrorException('Devices for activation must have sim`s')

    def __change_device_status(self, action: str, device):
        """
        Hidden method for changing status of the device
        Enabling a device have a two actions:
            - enable the endpoint
            - activate the assigned SIM
        Disabling a device have a two actions:
            - disable the device
            - suspend the assigned SIM
        """
        status_dict = {
            'enable': {
                'sim_status': emnify_constants.SimStatuses.ACTIVATED_DICT.value,
                'device_status': emnify_constants.DeviceStatuses.ENABLED_DICT.value
            },
            'disable': {
                'sim_status': emnify_constants.SimStatuses.SUSPENDED_DICT.value,
                'device_status': emnify_constants.DeviceStatuses.DISABLED_DICT.value
            }
        }

        device_for_update = self.device_update_model(status=status_dict[action]['device_status'])
        self.update_device(device_id=device.id, device=device_for_update)
        if device.sim:
            sim_update_model = self.client.sim.sim_update_model(status=status_dict[action]['sim_status'])
            self.client.sim.update_sim(sim_id=device.sim.id, sim=sim_update_model)
        return True

    @staticmethod
    def transform_all_devices_filter_params(query_params: GetDeviceFilterSet) -> dict:
        query_filter = {}
        filter_dict = query_params.dict(exclude_none=True)

        if filter_dict.get('q'):
            query_filter['q'] = ','.join(
                [f'{j}:{n}' for filter_values in filter_dict['q'] for j, n in filter_values.items()]
            )

        if filter_dict.get('sort'):
            query_filter['sort'] = ','.join([str(i) for i in filter_dict['sort']])
        return query_filter
