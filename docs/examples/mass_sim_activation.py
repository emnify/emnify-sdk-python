from emnify import EMnify
from emnify import constants
from emnify.errors import EMnifyBaseException

# === Example: Get your first device online ===

# To operate the emnify SDK, you need to generate an application token.
# Step-by-step guide: https://www.emnify.com/developer-blog/how-to-use-an-application-token-for-api-authentication
token = input("token: ")
# Authorize the client to perform operations:
emnify_client = EMnify(token)

# Before going online, you need a device and a SIM card.
# This example assumes you have a batch of SIM cards for your devices.
sim_batch_BIC2 = input("BIC2: ")

# emnify allows you to control your service and coverage policies.
# You can find those IDs on the Portal: https://portal.emnify.com/device-policies
service_profile_id = input("Service Profile ID: ")
tariff_profile_id = input("Tariff Profile ID: ")
# Then, you need service and coverage profiles to create devices later:
service_profile = emnify_client.devices.service_profile_model(
    id=int(service_profile_id)
)
tariff_profile = emnify_client.devices.tariff_profile_model(id=int(tariff_profile_id))

try:
    # Next, add the SIM card batch to your account.
    # This method also supports single SIM registration via BIC1
    # so you can use your free Trial SIMs.
    issued_sims = emnify_client.sim.register_sim(bic=sim_batch_BIC2)
    # All added SIMs are now registered with "Issued" status.
except EMnifyBaseException as e:
    # If an error appears during SIM registration,
    # use EMnifyBaseException for general exceptions
    # or inherited classes for specific ones.
    raise AssertionError(f"error during sim batch BIC2 activation{e}")

# Define the device status to apply when creating the device.
# In this example, the device status would be "Enabled"
device_status = emnify_client.devices.status_model(
    **constants.DeviceStatuses.ENABLED_DICT.value
)


for sim in issued_sims:
    # Only registering a SIM card won't provide connectivity.
    # You also need to create a new device with the SIM assigned.

    # To do this, specify the parameters of the device:
    device_name = f"Device({sim.iccid})"
    device_model = emnify_client.devices.device_create_model(
        tariff_profile=tariff_profile,
        status=device_status,
        service_profile=service_profile,
        sim=sim,
        name=device_name,
    )
    # See the API Reference to learn other device parameters:
    # https://emnify.github.io/emnify-sdk-python/autoapi/index.html

    # Then, create the device:
    device_id = emnify_client.devices.create_device(device=device_model)

    # Once created, you can retrieve the device information.
    # You can store this information in your local inventory for future needs.
    device = emnify_client.devices.retrieve_device(device_id=device_id)

    # Connectivity is turned off by default (so you aren't billed).
    # The following command enables connectivity for your device:
    emnify_client.devices.change_status(enable=True, device=device)

    # At this point, emnify can provide connectivity services.
    # You can send and receive SMS (if enabled in the assigned Service Profile).

    # To access the internet, configure the APN for your device.

    # The emnify APN is: em (two characters, no spaces)
    # This configuration may vary by the device manufacturer.
    # See the emnify Documentation: https://docs.emnify.com/apn-configuration

    # The following example sends a special configuration SMS command:
    ACTIVATION_CODE = 'AT+CGDCONT=1,"IP","em",,'
    SENDER = "city_scooters_admin"

    activation_sms = emnify_client.devices.sms_create_model(
        payload=ACTIVATION_CODE, source_adress=SENDER
    )

    # Finally, send the configuration SMS to your device:
    emnify_client.devices.send_sms(device=device, sms=activation_sms)

    # Congratulations! Your device is online.
    # If you run into problems using this example, please open an issue.
