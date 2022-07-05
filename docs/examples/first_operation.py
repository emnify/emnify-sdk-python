TOKEN = '<PASTE YOUR APPLICATION TOKEN HERE>'

# Import package
from emnify import EMnify

# Initiate SDK instance using application token

emnify = EMnify(TOKEN)

# Execute a command against desired API
devices = emnify.devices.get_devices_list()

# Showing all the devices
print([device for device in devices])
