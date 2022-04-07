# 1) Import SDK package
from emnify import EMnify

# 2) Initiate instance
emnify = EMnify(TOKEN)

# 3) Get all devices
devices = emnify.devices.get_all_devices();

# more about devices in [manager docs](../../../emnify/models/device/manager.html)
