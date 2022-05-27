import typing
from emnify.errors import UnexpectedArgumentException
from emnify.generated.models import Event
import emnify.models.device.api_call_manager as device_call_managers
from emnify.models.device.models import Device


class DeviceManager:
    def __init__(self, client):
        self.client = client

    @property
    def device_model(self):
        return Device

    def get_all_devices(self):
        """

        :return: Generator with Device objects
        """
        devices_response = device_call_managers.GetAllDevicesApiCall().call_api(client=self.client)
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
        events_response = device_call_managers.GetEventsByDevice().call_api(client=self.client, path_params=device_id)
        for event in events_response:
            yield Event(**event)
