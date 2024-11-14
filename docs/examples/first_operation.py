import os

# Import package
from emnify import EMnify

# Get the token from environment variable
TOKEN = os.environ.get("EMNIFY_APPLICATION_TOKEN")

# Initiate SDK instance using application token
emnify = EMnify(TOKEN)

# Execute a command against desired API
devices = emnify.devices.get_devices_list()

# Showing all the devices
print([device for device in devices])
