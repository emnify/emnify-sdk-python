***EMnify Python SDK***

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
        devices = emnify.devices.get_devices_list()  # Note: in 'devices' object-generator
        
- recieve events by device/device_id

        from emnify import EMnify
  
        emnify = EMnify(TOKEN)
        devices = emnify.devices.get_devices_list()  # Note: in 'devices' object-generator

- Getting Help
    - “If you need help installing or using the library, please [file a support ticket](https://support.emnify.com/hc/en-us/requests/new).
        
    -    If you've instead found a bug in the library or would like new features added, go ahead and open issues or pull requests against this repo.”
    
