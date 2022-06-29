Examples
========

.. |tag_device_creation| replace:: Device Creation
.. |tag_device_retrieve| replace:: Retrieve Device Details
.. |tag_device_activation| replace:: Device Activation/Deactivation
.. |tag_sim_register| replace:: SIM Registration
.. |tag_sim_assign| replace:: SIM Assignment
.. |tag_error_handling| replace:: Error Handling
.. |tag_sim_list| replace:: List SIMs

Get First Devices Online
~~~~~~~~~~~~~~~~~~~~~~~~

In order to get your devices online, you gonna need to perform a set of steps below.
This example demonstrates complex operation across multiple SDK :doc:`concepts`.

* `Device Policies <https://portal.emnify.com/device-policies>`_ that configure which services and where are gonna be available.
* You can learn more about APN configuration via SMS in `this article <https://support.emnify.com/hc/en-us/articles/4401906757906-How-to-configure-the-APN-on-different-devices>`_.
* |tag_sim_register|
* |tag_device_creation|
* |tag_sim_assign|
* |tag_error_handling|
* |tag_device_retrieve|
* |tag_device_activation|

.. literalinclude:: ../examples/mass_sim_activation.py
   :language: python
   :caption: mass_sim_activation.py
   :linenos:


Device Lifecycle Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initialization of SDK client
****************************

.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :end-before: [endblock]
   :linenos:

Create and activate a device
****************************

* |tag_device_creation|
* |tag_sim_register|
* |tag_sim_list|
* |tag_device_retrieve|
* |tag_device_activation|

.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at: Create and activate a device
   :end-before: [endblock]
   :linenos:


Configure a device
******************

If you want to avoid using a specific operator to avoid unintentional spending on the device,
you can add it to the blacklist of the device.

.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at:  Configure a device
   :end-before: [endblock]
   :linenos:


Configure operator blacklist for device
***************************************


.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at:  Configure operator blacklist for device
   :end-before: [endblock]
   :linenos:


Disable device
**************


.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at:  Disable device
   :end-before: [endblock]
   :linenos:


Delete device
*************


.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at:  Delete device
   :end-before: [endblock]
   :linenos:


Filtering and Sorting
~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../examples/filtering_and_sorting.py
   :language: python
   :caption: filtering_and_sorting.py
   :linenos:


Manage device connectivity
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at:  Manage device connectivity
   :end-before: [endblock]
   :linenos:
