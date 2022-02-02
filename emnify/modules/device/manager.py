import typing
import emnify.modules.device.api_call_manager as device_call_managers
from emnify.errors import UnexpectedArgumentException
from emnify.modules.device.models import Device, GetDeviceFilterSet, QFilterDeviceListQueryParam, DeviceEvent, \
    DeviceStatus, TariffProfile, ServiceProfile
from emnify.const import DeviceSortEnum


class DeviceManager:
    def __init__(self, client):
        self.client = client

    @property
    def device_model(self):
        return Device

    @property
    def event_model(self):
        return DeviceEvent

    @property
    def status_model(self):
        return DeviceStatus

    @property
    def service_profile_model(self):
        return ServiceProfile

    @property
    def tariff_profile_model(self):
        return TariffProfile

    @property
    def get_sort_device_param_enum(self):
        return DeviceSortEnum

    @property
    def get_device_list_filterset(self):
        return GetDeviceFilterSet

    @property
    def get_device_q_filterset(self) -> typing.Type[QFilterDeviceListQueryParam]:
        return QFilterDeviceListQueryParam

    def get_all_devices(self, *args, query_params: GetDeviceFilterSet = None, **kwargs):

        if query_params:
            query_params = self.transform_all_devices_filter_params(query_params)
        devices_response = device_call_managers.GetAllDevicesApiCall()\
            .call_api(client=self.client, query_params=query_params, *args, **kwargs)
        for device in devices_response:
            yield Device(**device)

    def get_device_events(self, device: typing.Union[Device, int]):
        """
        :param device: Device pydantic model or int
        :return: Generator with Device objects
        """
        if isinstance(device, Device):
            device_id = device.id
        elif isinstance(device, int):
            device_id = device
        else:
            raise UnexpectedArgumentException('device must be Device instance or int')
        events_response = device_call_managers.GetEventsByDevice().call_api(
            client=self.client, path_params={'endpoint_id': device_id}
        )
        for event in events_response:
            yield DeviceEvent(**event)

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

    def create_device(self, device: Device):
        if not isinstance(device, self.device_model):
            raise UnexpectedArgumentException('Argument must contain filled Device model')
        return device_call_managers.CreateDevice().call_api(client=self.client, data=device.dict(exclude_none=True))
