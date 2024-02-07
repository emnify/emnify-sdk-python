# === Example: Initialize the SDK client ===

from emnify import EMnify
from emnify import constants as emnify_constants

# To operate the emnify SDK, you need to generate an application token.
# Step-by-step guide: https://www.emnify.com/developer-blog/how-to-use-an-application-token-for-api-authentication
emnify = EMnify(app_token='YOUR_TOKEN')

# [endblock]

# === Example: Create and activate a device ===

unassigned_sims = [i for i in emnify.sim.get_sim_list(without_device=True)]
#  If there aren't any unassigned SIMs, register a new one via batch code:
if not unassigned_sims:
    registered_sim = emnify.sim.register_sim(bic='EXAMPLE_BIC_CODE') # Returns a list
    sim = emnify.sim.retrieve_sim(registered_sim[0].id)
else:
    sim = unassigned_sims[0]  # Takes the first unassigned SIM

# To create your new device, you need to define the parameters.
# You can retrieve all required models through the manager properties.
# API reference: https://emnify.github.io/emnify-sdk-python/autoapi/emnify/modules/device/manager/index.html
service_profile = emnify.devices.service_profile_model(id=1)
tariff_profile = emnify.devices.tariff_profile_model(id=1)
device_status = emnify.devices.status_model(id=0)
name = 'new_device'
device_model = emnify.devices.device_create_model(
    tariff_profile=tariff_profile,
    status=device_status,
    service_profile=service_profile,
    sim=sim,
    name=name
)

# After creating a model, the SDK returns the device ID.
device_id = emnify.devices.create_device(device=device_model)
# Then, you can retrieve the device details
device = emnify.devices.retrieve_device(device_id=device_id)
# and finally, activate the device:
emnify.devices.change_status(device=device, enable=True)

# Retrieve updated device details
device = emnify.devices.retrieve_device(device_id=device_id)
device_status = device.status.description  # Device status is "Enabled"
sim_status = device.sim.status.description  # SIM status is "Activated"

# [endblock]

# === Example: Configure a device ===

# Get device details
device = emnify.devices.retrieve_device(device_id=device_id)

tags = 'arduino, meter, temp'  # Example tags
name = 'new name'  # Example name

# Adjust the device configuration
update_device_fields = emnify.devices.device_update_model(name='new name', tags='arduino')
emnify.devices.update_device(device_id=device.id, device=update_device_fields)

# Get updated device details
updated_device = emnify.devices.retrieve_device(device_id=device_id)
device_tags = updated_device.tags  # Updated tag is "arduino"
deivce_name = updated_device.name  # Updated name is "new name"
# [endblock]

# === Example: Configure operator blacklist for a device ===

# Retrieve a list of all operators
all_operators = [i for i in emnify.operator.get_operators()]

# Add three operators to the blacklist:
device_id = 0  # Your device ID
emnify.devices.add_device_blacklist_operator(operator_id=all_operators[0].id, device_id=device_id)
emnify.devices.add_device_blacklist_operator(operator_id=all_operators[1].id, device_id=device_id)
emnify.devices.add_device_blacklist_operator(operator_id=all_operators[2].id, device_id=device_id)

# Get all blacklist operators of the device by device ID:
device_blacklist = emnify.devices.get_device_operator_blacklist(device_id=device_id)

operator_id = 0
for operator in device_blacklist:
    print(operator.country)
    print(operator.id)
    print(operator.mnc)
    operator_id = operator.id

# Removes the last operator from the blacklist
emnify.devices.delete_device_blacklist_operator(device_id=device_id, operator_id=operator_id)

# [endblock]

# === Example: Disable a device ===

# Get a list of all devices with SIM cards and the "Enabled" device status
device_filter = emnify.devices.get_device_filter_model(status=emnify_constants.DeviceStatuses.ENABLED_ID.value)
all_devices_with_sim = [
    device for device in emnify.devices.get_devices_list(filter_model=device_filter) if device.sim
]

device = all_devices_with_sim[0]

# Disable a device
emnify.devices.change_status(disable=True, device=device.id)

disabled_device = emnify.devices.retrieve_device(device_id=device.id)
device_status = disabled_device.status.description  # Device status is "Disabled"
sim_status = disabled_device.sim.status.description # SIM status is "Suspended"

# [endblock]

# === Example: Delete a device ===

# Get a list of all devices
old_devices_list = [device for device in emnify.devices.get_devices_list()]

device_to_delete = list(
        filter(
            lambda device: device.sim and device.status.id == emnify_constants.DeviceStatuses.ENABLED_ID,
            old_devices_list
        )
)[0]

# Choose a device to delete with an assigned SIM and the "Enabled" device status
sim_id_of_deleted_device = device_to_delete.sim.id

# Delete the device
emnify.devices.delete_device(device_id=device_to_delete.id)

# Retrieve a new list of all devices
new_device_list = [device for device in emnify.devices.get_devices_list()]

# Once your device is deleted, the total device count should be lower:
assert len(old_devices_list) > len(new_device_list)

sim = emnify.sim.retrieve_sim(sim_id=sim_id_of_deleted_device)
sim_status = sim.status.description  # SIM status is 'Suspended'

# [endblock]

# === Example: Manage device connectivity ===

# There are many reasons why connection issues arise. 
# For example:
# - The device executes the wrong procedures due to a bad firmware update.
# - The device executes network registration too frequently, so the network no longer allows it to register.
# - You changed a policy due to a blocked device.

# To reset device connectivity, use the following methods: 
# - Reset the device's connectivity
device_id = 0
emnify.devices.reset_connectivity_data(device_id=device_id)
# - Reset the network connectivity
emnify.devices.reset_connectivity_network(device_id=device_id)

# Use the following method to check the connectivity:
connectivity = emnify.devices.get_device_connectivity_status(device_id=device_id)
print(connectivity.status.description)  # Status is either "Attached", "Online", "Offline", or "Blocked"

# [endblock]
