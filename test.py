import settings
from emnify import EMnify

emnify = EMnify(settings.TOKEN)
sort = emnify.devices.get_sort_device_param_enum
filter = emnify.devices.get_device_q_filterset()
filter.name = 'First Device (Example'
filter.status = 1

filter_params = emnify.devices.get_device_list_filterset(q=[filter], sort=[sort.CREATED, sort.NAME])

devices = emnify.devices.get_all_devices(query_params=filter_params)
for device in devices:
    print(device)
    device_events = emnify.devices.get_device_events(device)
    for event in device_events:
        print(event)
