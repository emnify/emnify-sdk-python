import typing
import emnify.modules.device.api_call_manager as device_call_managers
from emnify.errors import UnexpectedArgumentException
from emnify.modules.device import models as device_models
from emnify.modules.operator import models as operator_models
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
        return device_models.Device

    @property
    def list_sms_model(self):
        return device_models.ListSms

    @property
    def device_detailed_model(self):
        return device_models.RetrieveDevice

    @property
    def sms_create_model(self):
        return device_models.SmsCreateModel

    @property
    def event_model(self):
        return device_models.DeviceEvent

    @property
    def status_model(self):
        return device_models.DeviceStatus

    @property
    def device_create_model(self):
        return device_models.CreateDevice

    @property
    def device_update_model(self):
        return device_models.UpdateDevice

    @property
    def service_profile_model(self):
        return device_models.ServiceProfile

    @property
    def tariff_profile_model(self):
        return device_models.TariffProfile

    @property
    def get_device_sort_enum(self):
        return emnify_constants.DeviceSort

    @property
    def get_device_filter_model(self) -> typing.Type[device_models.FilterDeviceModel]:
        return device_models.FilterDeviceModel

    def get_device_sms_list(self, *, device: typing.Union[device_models.Device, int]) -> device_models.ListSms:
        device_id = self.validate_device(device)
        sms_response = device_call_managers.GetAllSmsFromDevice().call_api(
            client=self.client, path_params={'endpoint_id': device_id}
        )
        for sms in sms_response:
            yield device_models.ListSms(**sms)

    def send_sms(
            self, *,
            device: typing.Union[device_models.Device, int, device_models.RetrieveDevice],
            sms: device_models.SmsCreateModel
    ) -> bool:
        """
        Method sends sms to device
        :param device: device model or id of device
        :param sms: SmsCreateModel
        :return: True if sms was sent
        """
        device_id = self.validate_device(device)
        if not isinstance(sms, device_models.SmsCreateModel):
            raise UnexpectedArgumentException('sms argument must be SmsCreateModel instance')
        return device_call_managers.SendSmsToDevice().call_api(
            client=self.client, path_params={'endpoint_id': device_id}, data=sms.dict(exclude_none=True)
        )

    def update_device(self, *, device_id: int, device: device_models.UpdateDevice) -> device_models.Device:
        """
        Method updates device
        :param device_id: id of device
        :param device: device update model
        :return: True if device was updated
        """
        return device_call_managers.UpdateDevice().call_api(
            client=self.client, data=device.dict(exclude_none=True), path_params={'endpoint_id': device_id}
        )

    def reset_connectivity_network(self, device_id: int) -> True:
        """
        Method resets device connectivity network
        :param device_id: id of device
        :return: True if reset of network was successful
        """
        return device_call_managers.ResetConnectivityPatch().call_api(
            client=self.client, path_params={'endpoint_id': device_id}, data={"location": None}
        )

    def reset_connectivity_data(self, device_id: int) -> True:
        """
        Method resets device connectivity data
        :param device_id: id of device
        :return: True if reset of data was successful
        """
        return device_call_managers.ResetConnectivityPatch().call_api(
            client=self.client, path_params={'endpoint_id': device_id}, data={"pdp_context": None}
        )

    def get_device_connectivity_status(self, device_id: int) -> device_models.DeviceConnectivityStatus:
        """
        Method returns device connectivity status
        :param device_id: id of device
        :return: DeviceConnectivityStatus model
        """
        return device_models.DeviceConnectivityStatus(**device_call_managers.GetDeviceConnectivity().call_api(
            client=self.client, path_params={'endpoint_id': device_id}
        ))

    def get_devices_list(
            self,
            *args,
            filter_model: device_models.FilterDeviceModel = None,
            sort_enum: device_models.DeviceSortModel = None,
            **kwargs
    ) -> typing.Generator[device_models.RetrieveDevice, None, None]:
        """
        Method returns list of devices
        :param filter_model: device filter model
        :param sort_enum: device sort enum
        :return: list of devices
        """
        query_params = None
        if filter_model or sort_enum:
            query_params = self.__transform_all_devices_filter_params(filter_model, sort_enum)
        devices_response = device_call_managers.GetAllDevicesApiCall()\
            .call_api(client=self.client, query_params=query_params, *args, **kwargs)
        return (device_models.Device(**i) for i in devices_response)

    def delete_device(self, device_id: int) -> True:
        """
        :param device_id: id of device
        :return: True if device was deleted
        """
        device = self.retrieve_device(device_id)
        if device.sim:
            self.release_sim(device_id)
        return device_call_managers.DeleteDevice().call_api(client=self.client, path_params={'endpoint_id': device_id})

    def add_device_blacklist_operator(self, device_id: int, operator_id: int) -> True:
        """
        :param device_id: id of device
        :param operator_id: id of operator
        :return: True if operator was added to blacklist
        """
        return device_call_managers.AddOperatorBlacklist().call_api(
            client=self.client, path_params={'endpoint_id': device_id, 'operator_id': operator_id}
        )

    def delete_device_blacklist_operator(self, device_id: int, operator_id: int):
        """
        :param device_id: id of device
        :param operator_id: id of operator
        :return: True if operator was deleted from blacklist
        """
        return device_call_managers.DeleteOperatorBlacklist().call_api(
            client=self.client, path_params={'endpoint_id': device_id, 'operator_id': operator_id}
        )

    def get_device_operator_blacklist(self, device_id: int):
        """
        :param device_id: id of device
        :return: list of operators
        """
        operators_json = device_call_managers.GetOperatorBlacklist().call_api(
            client=self.client, path_params={'endpoint_id': device_id}
        )
        for operator in operators_json:
            yield operator_models.Operator(**operator)

    def get_device_events_list(self, device: typing.Union[device_models.Device, int]):
        """
        :param device: Device pydantic-model or int
        :return: Generator with Device objects
        """
        device_id = self.validate_device(device)
        events_response = device_call_managers.GetEventsByDevice().call_api(
            client=self.client, path_params={'endpoint_id': device_id}
        )

        return (device_models.DeviceEvent(**i) for i in events_response)

    def change_status(
            self, device: typing.Union[
                device_models.UpdateDevice, device_models.Device, device_models.RetrieveDevice, int
            ],
            enable: bool = None, disable: bool = None
    ) -> None:
        """
        Change the status of a device and assigned SIM to enabled or disabled.

        :param device: The ID or device model to update.
        :type device: Union[UpdateDevice, Device, RetrieveDevice, int]
        :param enable: Whether to enable the device.
        :type enable: bool
        :param disable: Whether to disable the device.
        :type disable: bool
        :raises ValidationErrorException: If neither `enable` nor `disable` is provided, or if both are provided.
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
        :param device_id: id of device
        :return: True if device was disabled
        """
        device_update = self.device_update_model(status=emnify_constants.DeviceStatuses.DISABLED_DICT.value)
        self.update_device(device=device_update, device_id=device_id)

    def release_sim(self, device_id: int):
        """
        This method allows to release the assigned SIM from device by device_id
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
            if sim.status.id == emnify_constants.SimStatusesID.SUSPENDED_ID.value:
                self.change_status(device.id, disable=True)
            elif sim.status.id == emnify_constants.SimStatusesID.ACTIVATED_ID.value:
                self.change_status(device.id, enable=True)

        self.update_device(device=self.device_update_model(sim={"id": sim.id}), device_id=device.id)

    def create_device(self, device: device_models.Device) -> bool:
        """
        Method for creating a device
        :param device: device model
        :return: True if device was created
        """
        if not isinstance(device, self.device_model):
            raise UnexpectedArgumentException('Argument must contain filled Device model')
        return device_call_managers.CreateDevice().call_api(client=self.client, data=device.dict(exclude_none=True))

    def retrieve_device(self, device_id: int) -> device_models.RetrieveDevice:
        if not isinstance(device_id, int) or device_id <= 0:
            raise UnexpectedArgumentException('Device id must be positive integer')
        response = device_call_managers.RetrieveDevice().call_api(
            client=self.client, path_params={'endpoint_id': device_id}
        )
        return device_models.RetrieveDevice(**response)

    @staticmethod
    def validate_device(device: device_models.Device) -> int:
        if isinstance(device, device_models.Device) or isinstance(device, device_models.RetrieveDevice):
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
        if status == emnify_constants.SimStatusesDict.ACTIVATED_DICT:
            if not device.sim:
                raise emnify_errors.ValidationErrorException('Devices for activation must have sim`s')

    def __change_device_status(self, action: str, device):
        """
        Hidden method for changing status of the device
        """
        status_dict = {
            'enable': {
                'sim_status': emnify_constants.SimStatusesDict.ACTIVATED_DICT.value,
                'device_status': emnify_constants.DeviceStatuses.ENABLED_DICT.value
            },
            'disable': {
                'sim_status': emnify_constants.SimStatusesDict.SUSPENDED_DICT.value,
                'device_status': emnify_constants.DeviceStatuses.DISABLED_DICT.value
            }
        }

        device_for_update = self.device_update_model(status=status_dict[action]['device_status'])
        self.update_device(device_id=device.id, device=device_for_update)
        if device.sim:
            sim_update_model = self.client.sim.get_sim_update_model(status=status_dict[action]['sim_status'])
            self.client.sim.update_sim(sim_id=device.sim.id, sim=sim_update_model)
        else:
            raise emnify_errors.ValidationErrorException('Can`t enable device without sim card')

        return True

    @staticmethod
    def __transform_all_devices_filter_params(
            filter_model: device_models.FilterDeviceModel = None,
            sort_enum: device_models.DeviceSortModel = None
    ) -> dict:
        query_filter = {}
        if filter_model:
            filter_dict = filter_model.dict(exclude_none=True)
            query_filter['q'] = ','.join([f'{key}:{filter_dict[key]}' for key in filter_dict])
        if sort_enum:
            query_filter['sort'] = sort_enum
        return query_filter
