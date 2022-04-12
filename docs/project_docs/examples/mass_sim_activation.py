from emnify import EMnify
from emnify.errors import EMnifyBaseException


"""
## Mass sim activation example
## Contains:
* [Classes Documentation](../../index.html)
* [Exceptions Documentation](../examples/exceptions_documentation.html)
* [Models Documentation](../examples/models.html)
"""

token = input('token: ')
sim_batch_BIC2 = input('BIC2: ')


emnify_client = EMnify(token)
# Use EMnifyBaseException for general exceptions or inherited classes for specific one`s
try:
    issued_sims = emnify_client.sim.register_sim(bic=sim_batch_BIC2)
#  After Sim batch is sended - all sim`s are registred with "issued" status
except EMnifyBaseException as e:
    raise AssertionError(f"error during sim batch BIC2 activation{e}")
service_profile = emnify_client.devices.service_profile_model(id=1)
tariff_profile = emnify_client.devices.tariff_profile_model(id=1)
device_status = emnify_client.devices.status_model(id=0)
for sim in issued_sims:
    device_name = f"Device({sim.iccid})"
# Sim status 1 - means sim is active
    sim.status = {"id": 1}
    device = emnify_client.devices.device_create_model(
        tariff_profile=tariff_profile, status=device_status, service_profile=service_profile, sim=sim
    )
    device_model = emnify_client.devices.retrieve_device(device_id=emnify_client.devices.create_device(device))
    activation_code = 'AT+CGDCONT=1,"IP","em",,'
    sender = "city_scooters_admin"
    activation_sms = emnify_client.devices.sms_create_model(payload=activation_code, source_adress=sender)
    emnify_client.devices.send_sms(device=device_model, sms=activation_sms)
