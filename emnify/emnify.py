import sys
import logging
from emnify import errors as emnify_errors
from .modules.device.manager import DeviceManager
from .modules.sim.manager import SimManager
from .modules.operator.manager import OperatorManager
logger = logging.getLogger('EmnifySDK')


class EMnify(object):
    """
    base SDK class
    token: Emnify api token
    """
    def __init__(self, app_token=None):
        if not sys.version_info >= (3, 9):
            raise emnify_errors.MinimalPythonVersionException('Python version 3.9 or higher is required')
        assert app_token
        self.app_token = app_token
        self.devices: DeviceManager = DeviceManager(self)
        self.sim: SimManager = SimManager(self)
        self.operator: OperatorManager = OperatorManager(self)
        self.token = None
