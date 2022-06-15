
# === Using a Filtering for List calls  ===
from emnify import EMnify
from emnify import constants as emnify_constants

emnify_client = EMnify(app_token='your_application_token')

# Some methods that return multiple objects allow sorting and filtering.
# This allows us to optimize processing time, since using filtering we can immediately get the necessary objects with
# the necessary qualities, and sorting allows us to set the order in which objects are displayed.
# Instead of sending several requests in search of the required object, we can reduce their number to one.

# For example - we want to find all SIM`s with specific customer organisation, first one for instance.
# We need to initiate the model for filtering by specifying the necessary parameters in it as arguments.
sim_filter = emnify_client.sim.get_sim_filter_model(customer_org=1)
# To get the filtering model for filling, you need to get it as a property of a manager
# for SIM cards, this would be get_sim_filter_model, for Devices it would be a get_device_filter_model

# After initializing the model object, it must be passed as an argument that makes a request to get a list of objects.
sims = emnify_client.sim.get_sim_list(filter_model=sim_filter)
# sims now contains the objects we need with client organization 1

# We can pass several parameters for filtering for a more detailed search for the necessary objects.
sim_filter = emnify_client.sim.get_sim_filter_model(
    customer_org=1,
    status=emnify_constants.SimStatusesID.ACTIVATED_ID.value,
    production_date='2019-01-25'
)

# The request to get a list of SIM cards also has a separate filter,
# which is passed as an argument to the filtering function - without a device.

sims_without_assigned_device = emnify_client.sim.get_sim_list(without_device=True)


# === Using a Sorting for List calls  ===
# Just like filtering, sorting allows us to reduce processing time by ordering objects in the server.
# Thus, it is easier for you to group objects according to a certain attribute by specifying it in sorting.

# For example - we want to get all devices sorted by last updated date
# All sorting is done by using enums
sort_parameter = emnify_client.devices.get_device_sort_enum.LAST_UPDATED.value

# After choosing a parameter for filtering, we need to pass it as an argument sort_enum
sorted_devices = emnify_client.devices.get_devices_list(
    sort_enum=sort_parameter
)

# Now we got a list of devices, at the beginning of which are the recently updated devices
for latest_device in sorted_devices:
    ...
