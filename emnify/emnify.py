import logging
from .modules.device.manager import DeviceManager
logger = logging.getLogger('EmnifySDK')


class EMnify(object):
    """
    base SDK class
    token: Emnify api token
    """
    def __init__(self, app_token=None):
        assert app_token
        self.app_token = app_token
        self.devices: DeviceManager = DeviceManager(self)
        self.token = None
