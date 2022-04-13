
# # Getting Started

"""
## Install
Python > 3.6 is required.

### Install from source
```
git clone https://github.com//emnify-python-sdk.git
cd emnify-python-sdk
python setup.py install
```
### or install with pip
```
pip install emnify-python-sdk
```
"""

# ## Create Application Token
"""
Create your application token on: [https://portal.emnify.com/integrations/](https://portal.emnify.com/integrations/), and copy it.
"""

# ## Use
TOKEN = 'test'

# 1) import package
from emnify import EMnify

# 2) initiate SDK instance using application token

emnify = EMnify(TOKEN)

# 3) Execute a command against desired API
devices = emnify.devices.get_devices_list()

"""
## Explore more
* Examples
* [Classes Documentation](../../index.html)
* Zendesk
"""
