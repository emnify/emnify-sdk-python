# This example is intended for local debugging purposes and is designed to work inside the Docker development environment.
# For more information, please refer to the DEVELOPMENT.md file.

import os
import sys

# Add the path to the module to the Python path, below it's set to Docker workdir
sys.path.append('/sdk')
# Import package
from emnify import EMnify

# Get the token from environment variable
TOKEN = os.environ.get('EMNIFY_APPLICATION_TOKEN')

# Initiate SDK instance using application token
emnify = EMnify(TOKEN)

# Execute a command against desired API
devices = emnify.devices.get_devices_list()

# Showing all the devices
print([device for device in devices])
