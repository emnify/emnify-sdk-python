from emnify import EMnify
from emnify import constants as emnify_constants

emnify = EMnify(app_token='your token')

#  Create and activate a device 


all_sims = emnify.sim.get_sim_list()
unassigned_sims = []
for sim in all_sims:
    if not sim.endpoint:
        unassigned_sims.append(sim)
#  If no unassigned_sims - register new one by batch code
registered_sim = emnify.sim.register_sim(bic='sample_bic_code')  # Returns as list
emnify.sim.issue_sim(registered_sim[0].id)
sim = emnify.sim.retrieve_sim(registered_sim[0].id)

service_profile = emnify.devices.service_profile_model(id=1)
tariff_profile = emnify.devices.tariff_profile_model(id=1)
device_status = emnify.devices.status_model(id=0)
device_model = emnify.devices.device_create_model(
        tariff_profile=tariff_profile, status=device_status, service_profile=service_profile, sim=sim
    )

# All required models can be retrieved through manager`s properties
device_id = emnify.devices.create_device(device=device_model)

# After creating model sdk returns id of device
device = emnify.devices.retrieve_device(device_id=device_id)
emnify.devices.change_status(device=device, enable=True)  # Activate device

device = emnify.devices.retrieve_device(device_id=device_id)
device_status = device.status.description  # Will be 'Enabled'
sim_status = device.sim.status.description  # Will be 'Activated'
# [endblock]

#  Configure a device 

device = emnify.devices.retrieve_device(device_id=device_id)
#  Getting details of device

ip_adress = '192.0.0.0'  # Sample ip_adress
name = 'new name'  # Sample name
update_device_fields = emnify.devices.device_update_model(name='new name', ip_address='192.0.0.0')
emnify.devices.update_device(device_id=device.id, device=update_device_fields)
# adjust device config

updated_device = emnify.devices.retrieve_device(device_id=device_id)
#  Getting details of updated device
device_ip_address = updated_device.ip_address  # Will be '192.0.0.0'
deivce_name = updated_device.name  # Will be 'new name'
# [endblock]

#  Configure operator blacklist for device 

all_operators = [i for i in emnify.operator.get_operators()]
# List of all operators

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

#  Disable device 


all_devices_with_sim = [
    device for device in emnify.devices.get_devices_list() if device.sim
    and device.status.id == emnify_constants.DeviceStatuses.ENABLED_ID.value
]
# Getting list of all devices with sim cards and enabled status

device = all_devices_with_sim[0]

emnify.devices.change_status(disable=True, device=device.id)
# Disable a device

disabled_device = emnify.devices.retrieve_device(device_id=device.id)
device_status = disabled_device.status.description  # Will be 'Disabled'
sim_status = disabled_device.sim.status.description # Will be 'Suspended'
# [endblock]

#  Delete device 

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