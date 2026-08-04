# * Import SDK package
from emnify import EMnify

#  Initiate instance

emnify_client = EMnify("YOUR APP TOKEN")
"""
=== Create a disabled device with a SIM that stays in ISSUED status ===
"""
# When a sim object is provided the API activates the SIM by default, and an
# activated SIM is billed even while the device is disabled. Pass
# `activate: False` to assign the SIM without activating it.
service_profile = emnify_client.devices.service_profile_model(id=1)
tariff_profile = emnify_client.devices.tariff_profile_model(id=1)
device_status = emnify_client.devices.status_model(id=1, description="Disabled")
device_model = emnify_client.devices.device_create_model(
    name="my-device",
    tariff_profile=tariff_profile,
    status=device_status,
    service_profile=service_profile,
    # pass a plain dict - the SimList model has no `activate` field and would drop it
    sim={"id": 1, "activate": False},
)

device_id = emnify_client.devices.create_device(device_model)

# The SIM is assigned to the device and still in ISSUED status
print(emnify_client.sim.retrieve_sim(sim_id=1).status)
