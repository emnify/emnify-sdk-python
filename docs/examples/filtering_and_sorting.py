
from emnify import EMnify
from emnify import constants as emnify_constants

# To operate the emnify SDK, you need to generate an application token.
# Step-by-step guide: https://www.emnify.com/developer-blog/how-to-use-an-application-token-for-api-authentication
emnify_client = EMnify(app_token='YOUR_TOKEN')

# Some methods that return multiple objects allow sorting and filtering.
# API reference: https://emnify.github.io/emnify-sdk-python/autoapi/index.html

# This optimizes processing time because:
# - Filtering lets you only retrieve the objects you need.
# - Sorting allows you to set the order that objects are displayed.
# Instead of sending several requests to get the required object, you only need one.

# === Example: Filter a list of SIM cards ===

# This example finds all SIMs for a specific customer organization.
# Start by initiating the model for filtering by specifying the necessary parameters as arguments.
sim_filter = emnify_client.sim.get_sim_filter_model(customer_org=1)

# Next, you need to get the filtering model for filling as a property of a manager.
# For SIM cards: get_sim_filter_model
# For devices: get_device_filter_model

# After initializing the model object, pass it as an argument to request a list of objects.
sims = emnify_client.sim.get_sim_list(filter_model=sim_filter)
# Now, sims contains the objects for customer organization 1.

# For a more detailed search, pass several parameters for filtering:
sim_filter = emnify_client.sim.get_sim_filter_model(
    customer_org=1,
    status=emnify_constants.SimStatusesID.ACTIVATED_ID.value,
    production_date='2019-01-25'
)

# The list SIM cards request also has a separate filter, passed as an argument.
# The following example searches for SIMs without a device:
sims_without_assigned_device = emnify_client.sim.get_sim_list(without_device=True)

# === Example: Sort a list of SIM cards ===

# Like filtering, sorting reduces processing time by ordering objects in the server.
# Sorting also enables you to group objects by specifying a particular attribute.

# The following example sorts all devices by the last updated date.
# Note: All sorting uses enums.
sort_parameter = emnify_client.devices.get_device_sort_enum.LAST_UPDATED.value

# After choosing a filtering parameter, pass it as an argument to sort_enum:
sorted_devices = emnify_client.devices.get_devices_list(
    sort_enum=sort_parameter
)

# Now, you have a list of devices with the most recently updated at the top.
for latest_device in sorted_devices:
    ...
