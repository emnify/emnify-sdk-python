import os
# Import the package
from emnify import EMnify

# Initiate the SDK instance using your application token
emnify = EMnify(os.environ["EMNIFY_TOKEN"])

# Execute a command against the desired API
devices = emnify.devices.get_devices_list()

# Show all the devices
print([device for device in devices])