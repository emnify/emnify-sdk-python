from emnify import EMnify
from emnify import constants as emnify_constants

emnify = EMnify(app_token='your token')
# [endblock]
#  === Create and activate a device ===


unassigned_sims = [i for i in emnify.sim.get_sim_list(without_device=True)]
#  If no unassigned_sims - register new one by batch code
if not unassigned_sims:
    registered_sim = emnify.sim.register_sim(bic='sample_bic_code')  # Returns as list
    sim = emnify.sim.retrieve_sim(registered_sim[0].id)
else:
    sim = unassigned_sims[0]  # Taking the first one unassigned sim

# Defining of new device parameters
# All required models can be retrieved through manager`s properties
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

# After creating model sdk returns id of device
device_id = emnify.devices.create_device(device=device_model)
# Then we can retrieve all device details
device = emnify.devices.retrieve_device(device_id=device_id)
# Activate device
emnify.devices.change_status(device=device, enable=True)

# Retrieving updated device details
device = emnify.devices.retrieve_device(device_id=device_id)
device_status = device.status.description  # Will be 'Enabled'
sim_status = device.sim.status.description  # Will be 'Activated'
# [endblock]

#  === Configure a device ===

#  Getting details of device
device = emnify.devices.retrieve_device(device_id=device_id)

tags = 'arduino, meter, temp'  # Sample tags
name = 'new name'  # Sample name

# Adjust device config
update_device_fields = emnify.devices.device_update_model(name='new name', tags='arduino')
emnify.devices.update_device(device_id=device.id, device=update_device_fields)

#  Getting details of updated device
updated_device = emnify.devices.retrieve_device(device_id=device_id)
device_tags = updated_device.tags  # Will be arduino
deivce_name = updated_device.name  # Will be 'new name'
# [endblock]

#  === Configure operator blacklist for device ===

# List of all operators
all_operators = [i for i in emnify.operator.get_operators()]

device_id = 0  # Your device id
emnify.devices.add_device_blacklist_operator(operator_id=all_operators[0].id, device_id=device_id)
emnify.devices.add_device_blacklist_operator(operator_id=all_operators[1].id, device_id=device_id)
emnify.devices.add_device_blacklist_operator(operator_id=all_operators[2].id, device_id=device_id)
# Adding 3 operators to the blacklist

device_blacklist = emnify.devices.get_device_operator_blacklist(device_id=device_id)
# Getting all blacklist operators of device by device_id

operator_id = 0
for operator in device_blacklist:
    print(operator.country)
    print(operator.id)
    print(operator.mnc)
    operator_id = operator.id

emnify.devices.delete_device_blacklist_operator(device_id=device_id, operator_id=operator_id)
# Removing the last operator from blacklist
# [endblock]

#  === Disable device ===

device_filter = emnify.devices.get_device_filter_model(status=emnify_constants.DeviceStatuses.ENABLED_ID.value)
all_devices_with_sim = [
    device for device in emnify.devices.get_devices_list(filter_model=device_filter) if device.sim
]
# Getting list of all devices with sim cards and enabled status

device = all_devices_with_sim[0]

emnify.devices.change_status(disable=True, device=device.id)
# Disable a device

disabled_device = emnify.devices.retrieve_device(device_id=device.id)
device_status = disabled_device.status.description  # Will be 'Disabled'
sim_status = disabled_device.sim.status.description # Will be 'Suspended'
# [endblock]

#  === Delete device ===

old_devices_list = [device for device in emnify.devices.get_devices_list()]
# Getting list of all devices

device_to_delete = list(
        filter(
            lambda device: device.sim and device.status.id == emnify_constants.DeviceStatuses.ENABLED_ID,
            old_devices_list
        )
)[0]
# Picking up a device to delete with assigned sim and enabled status

sim_id_of_deleted_device = device_to_delete.sim.id

emnify.devices.delete_device(device_id=device_to_delete.id)
# Deleting a device

new_device_list = [device for device in emnify.devices.get_devices_list()]
# Getting new list of all devices


assert len(old_devices_list) > len(new_device_list)
# After deleting count of all devices will be lowered

sim = emnify.sim.retrieve_sim(sim_id=sim_id_of_deleted_device)
sim_status = sim.status.description  # Will be 'Suspended'

# [endblock]


#  === Manage device connectivity ===

# Lookup for documentation for learn more
# https://www.emnify.com/developer-blog/5-ways-to-detect-and-solve-connectivity-issues#network-events

# There are many reasons why connection issues arise. For example:
# * The device executes the wrong procedures due to a bad firmware update.
# * The device executes network registration too frequently that the network no longer allows it to register.
# * You have simply changed a policy due to a blocked device.

# For resetting a device connectivity you can use the following methods:
# * Resetting the connectivity of device
device_id = 0
emnify.devices.reset_connectivity_data(device_id=device_id)
# * Resetting the connectivity
emnify.devices.reset_connectivity_network(device_id=device_id)

# For checking connectivity you can use the method:
connectivity = emnify.devices.get_device_connectivity_status(device_id=device_id)
print(connectivity.status.description)  # Will be 'ATTACHED'/'ONLINE'/'OFFLINE'/'BLOCKED'

# [endblock]
