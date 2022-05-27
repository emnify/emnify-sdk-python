import logging
from .models.device.manager import DeviceManager
logger = logging.getLogger('EmnifySDK')


class EMnify(object):
    """
    base SDK class
    token: Emnify api token
    """
    def __init__(self, token=None):
        assert token
        self.token = token
        self.devices: DeviceManager = DeviceManager(self)
