from emnify import EMnify
from emnify import constants
from emnify.errors import EMnifyBaseException

# === Massive SIM Activation Example ===

# Define Application token and BIC2 for the SIM batch we want to activate.
token = input('token: ')
sim_batch_BIC2 = input('BIC2: ')
# [Device Policies Configuration](https://portal.emnify.com/device-policies), you can find IDs there.
service_profile_model_id = input('service_profile_id: ')
tariff_profile_model_id = input('tariff_profile_id: ')
emnify_client = EMnify(token)

try:
    issued_sims = emnify_client.sim.register_sim(bic=sim_batch_BIC2)
# After Sim batch is sended - all sim`s are registred with "issued" status
except EMnifyBaseException as e:
# Use EMnifyBaseException for general exceptions or inherited classes for specific one`s
    raise AssertionError(f"error during sim batch BIC2 activation{e}")

# In order to create devices for SIMs afterwards we need service and coverage profiles.
service_profile = emnify_client.devices.service_profile_model(id=int(service_profile_model_id))
tariff_profile = emnify_client.devices.tariff_profile_model(id=int(tariff_profile_model_id))

# We define status of device to be applied during creation.
device_status = emnify_client.devices.status_model(
    **constants.DeviceStatuses.ENABLED_DICT.value
)

for sim in issued_sims:
    # Here we create a new device with the SIM assigned.
    # It will be activated after device creation.
    device_name = f"Device({sim.iccid})"

    device_model = emnify_client.devices.device_create_model(
        tariff_profile=tariff_profile,
        status=device_status,
        service_profile=service_profile,
        sim=sim,
        name=device_name
    )

    device_id = emnify_client.devices.create_device(device=device_model)
    # After creation we may retrieve device information.
    device = emnify_client.devices.retrieve_device(device_id=device_id)
    emnify_client.devices.change_status(enable=True, device=device)

    # After making sure device is created and enabled we send there configuration SMS.
    # It may vary on device manufacturer.
    ACTIVATION_CODE = 'AT+CGDCONT=1,"IP","em",,'
    SENDER = "city_scooters_admin"

    activation_sms = emnify_client.devices.sms_create_model(
        payload=ACTIVATION_CODE,
        source_adress=SENDER
    )
    emnify_client.devices.send_sms(device=device, sms=activation_sms)
