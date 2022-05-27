***EMify python SDK***

How to install

Python > 3.6 is required.



- Install from source
>       git clone https://github.com//emnify-python-sdk.git
>       cd emnify-python-sdk
>       python setup.py install
- or install with pip
>        pip install emnify-python-sdk
  
> Create your application token on: https://portal.emnify.com/integrations/

**Example**

- recieve all devices

        from emnify import EMnify
  
        emnify = EMnify(TOKEN)
        devices = emnify.devices.get_all_devices()  # Note: in 'devices' object-generator
        
- recieve events by device/device_id

        from emnify import EMnify
  
        emnify = EMnify(TOKEN)
        devices = emnify.devices.get_all_devices()  # Note: in 'devices' object-generator
