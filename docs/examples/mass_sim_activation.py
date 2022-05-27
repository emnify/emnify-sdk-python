from emnify import EMnify
from emnify import constants
from emnify.errors import EMnifyBaseException


"""
# Massive SIM Activation Example
"""

# Define Application token and BIC2 for the SIM batch we want to activate.
token = input('token: ')
sim_batch_BIC2 = input('BIC2: ')

emnify_client = EMnify(token)
try:
    issued_sims = emnify_client.sim.register_sim(bic=sim_batch_BIC2)
# After Sim batch is sended - all sim`s are registred with "issued" status
except EMnifyBaseException as e:
# Use EMnifyBaseException for general exceptions or inherited classes for specific one`s
    raise AssertionError(f"error during sim batch BIC2 activation{e}")

# In order to create devices for SIMs afterwards we need service and coverage profiles.
# [Device Policies Configuration](https://portal.emnify.com/device-policies), you can find IDs there.
service_profile = emnify_client.devices.service_profile_model(id=1)
tariff_profile = emnify_client.devices.tariff_profile_model(id=1)

# We define status of device to be applied during creation.
device_status = emnify_client.devices.status_model(id=0)

for sim in issued_sims:
    device_name = f"Device({sim.iccid})"
    sim.status = {constants.SimStatusesDict.ACTIVATED_DICT.value}
# Here we create a new device with the SIM assigned. It will be activated after device creation.
    device = emnify_client.devices.device_create_model(
        tariff_profile=tariff_profile, status=device_status, service_profile=service_profile, sim=sim
    )
# After creation we may retrieve device information.
    device_model = emnify_client.devices.retrieve_device(device_id=emnify_client.devices.create_device(device))

# After making sure device is created we send there configuration SMS. It may vary on device manufacturer. You can learn more about SMS configuration in [this article](https://support.emnify.com/hc/en-us/articles/4401906757906-How-to-configure-the-APN-on-different-devices).
    activation_code = constants.Example.ACTIVATION_CODE.value
    sender = constants.Example.SENDER.value
    activation_sms = emnify_client.devices.sms_create_model(payload=activation_code, source_adress=sender)
    emnify_client.devices.send_sms(device=device_model, sms=activation_sms)
