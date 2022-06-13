from emnify import EMnify
from emnify import constants
from emnify.errors import EMnifyBaseException

# === Example: Getting First Devices Online ===

# To operate EMnify SDK you need to generate application token.
# That is how: https://www.emnify.com/developer-blog/how-to-use-an-application-token-for-api-authentication
token = input('token: ')
# The client is authorized to perform operations by your name;
emnify_client = EMnify(token)

# There are two things you need to obtain before you get you device online,
# one is a device and other is a SIM card.
# For this example we assume you have a batch of SIM cards you willing to
# use in your devices.
sim_batch_BIC2 = input('BIC2: ')

# EMnify allows you to control coverage and services you need.
# Lookup Concepts to learn more.
# https://portal.emnify.com/device-policies you can find IDs there.
service_profile_id = input('Service Profile ID: ')
tariff_profile_id = input('Tariff Profile ID: ')
# In order to create devices for SIMs afterwards we need service and coverage profiles.
service_profile = emnify_client.devices.service_profile_model(id=int(service_profile_id))
tariff_profile = emnify_client.devices.tariff_profile_model(id=int(tariff_profile_id))

try:
    # Having a batch of SIM cards you need to add them to your account;
    # This method also supports single sim registration via BIC1,
    # so you can use your FREE Evaluation SIM cards either;
    issued_sims = emnify_client.sim.register_sim(bic=sim_batch_BIC2)
    # After it's added - all sim`s are registred with "issued" status;
except EMnifyBaseException as e:
    # It can happen that there is some error appear during SIM registration;
    # Use EMnifyBaseException for general exceptions or inherited classes for specific one`s;
    raise AssertionError(f"error during sim batch BIC2 activation{e}")

# We define status of device to be applied during creation.
device_status = emnify_client.devices.status_model(
    **constants.DeviceStatuses.ENABLED_DICT.value
)


for sim in issued_sims:
    # SIM cards do not provide connectivity by just registering them,
    # So in order to get devices you put SIM cards in you also need to
    # create a new device with the SIM assigned.

    # For device creation we need to specify parameters of the device:
    device_name = f"Device({sim.iccid})"
    device_model = emnify_client.devices.device_create_model(
        tariff_profile=tariff_profile,
        status=device_status,
        service_profile=service_profile,
        sim=sim,
        name=device_name
    )
    # See API Reference to learn other parameters the device can have.

    # And there is how we create a device we wanted.
    device_id = emnify_client.devices.create_device(device=device_model)

    # After creation we may retrieve full device information.
    # Which you can store in your local inventory for future needs.
    device = emnify_client.devices.retrieve_device(device_id=device_id)

    # As it mentioned above by default connectivity is disabled so you're not getting billed.
    # The following command will enable connectivity for your device with a SIM card installed.
    emnify_client.devices.change_status(enable=True, device=device)
    # At this point EMnify is ready to provide you connectivity services.
    # So we can already send and receive SMS(if this enabled in the Service Profile assigned).

    # After making sure device is created and enabled
    # it is time to perform configuration on a device side.

    # Correct APN configuration of the device is required to access internet.
    # EMnify APN is(no spaces, just two characters): em
    # For example purposes we will send a special configuration SMS command.
    # It may vary by the device manufacturer, see our documentation to learn
    # if this method suites your devices.
    ACTIVATION_CODE = 'AT+CGDCONT=1,"IP","em",,'
    SENDER = "city_scooters_admin"

    activation_sms = emnify_client.devices.sms_create_model(
        payload=ACTIVATION_CODE,
        source_adress=SENDER
    )

    # And now we send the configuration SMS to our device.
    emnify_client.devices.send_sms(device=device, sms=activation_sms)

    # CONGRATULATIONS! You get your device online!
    # Now you can check your device internet access.
