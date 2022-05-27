import settings
from emnify import EMnify

emnify = EMnify(settings.TOKEN)

devices = emnify.devices.get_all_devices()
for device in devices:
    print(device)
    device_events = emnify.devices.get_device_events(device)
    for event in device_events:
        print(event)
