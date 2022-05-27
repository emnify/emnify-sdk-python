import vcr
from emnify import EMnify

sdk_client = EMnify(app_token='test')

with vcr.use_cassette('fixtures/vcr_cassettes/get_all_devices.yaml'):
    devices = [i for i in sdk_client.devices.get_devices_list()]

with vcr.use_cassette('fixtures/vcr_cassettes/device_events.yaml'):
    device_events = [i for i in sdk_client.devices.get_device_events_list(devices[3])]

device_to_update = devices[0]
device_to_update.status = 1

sdk_client.devices.update_device(device=device_to_update, device_id=device_to_update.id)


with vcr.use_cassette('fixtures/vcr_cassettes/create_device_with_sim.yaml'):
    pass
