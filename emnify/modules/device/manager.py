import typing
import emnify.modules.device.api_call_manager as device_call_managers
from emnify.errors import UnexpectedArgumentException
from emnify.modules.device.models import Device, GetDeviceFilterSet, QFilterDeviceListQueryParam, DeviceEvent, \
    DeviceStatus, TariffProfile, ServiceProfile, ListSms, SmsCreateModel, RetrieveDevice, UpdateDevice, CreateDevice
from emnify.const import DeviceSortEnum


class DeviceManager:
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
    def service_profile_model(self):
        return ServiceProfile

    @property
    def tariff_profile_model(self):
        return TariffProfile

    @property
    def sort_device_param_enum(self):
        return DeviceSortEnum

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

    def send_sms(self, *args, device: typing.Union[Device, int], sms: SmsCreateModel) -> bool:
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
        if isinstance(device, Device):
            return device.id
        elif isinstance(device, int):
            return device
        else:
            raise UnexpectedArgumentException('device must be Device instance or int')

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