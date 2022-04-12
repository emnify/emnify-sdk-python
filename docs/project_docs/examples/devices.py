# * Import SDK package
from emnify import EMnify

#  Initiate instance

emnify_client = EMnify('YOUR APP TOKEN')
"""
=== Get all devices ===
"""
devices = emnify_client.devices.get_devices_list()
"""
=== Create device ===
"""
service_profile = emnify_client.devices.service_profile_model(id=1)
tariff_profile = emnify_client.devices.tariff_profile_model(id=1)
device_status = emnify_client.devices.status_model(id=0)
device_model = emnify_client.devices.device_create_model(
        tariff_profile=tariff_profile, status=device_status, service_profile=service_profile
    )
# All required models can be retrieved through manager`s properties

device_id = emnify_client.devices.create_device(device_model)

# more about sdk models in [manager docs](../../../emnify/models/device/manager.html)
# more about devices in [manager docs](../../../emnify/models/device/manager.html)
