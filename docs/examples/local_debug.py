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

def get_iterator_length(iterator):
    return len(list(iterator))

# Execute a command against desired API
devices = emnify.devices.get_devices_list()


## print first 100 devices
for i, device in enumerate(devices):
    if i >= 100:
        break
    print(device)

# Count remaining devices
print(get_iterator_length(devices))


# Get list of sims
sims = emnify.sim.get_sim_list()

# Count sims
print(get_iterator_length(sims))

