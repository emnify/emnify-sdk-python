
from emnify.generated.models import Endpoint


class Device(Endpoint):
    pass


class DeviceIdRequired(Device):
    id: int
