Examples
========

Massive SIM Activation
~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates complex operation across multiple SDK Concepts.

* `Device Policies <https://portal.emnify.com/device-policies>`_ that configure which services and where are gonna be available.
* You can learn more about APN configuration via SMS in `this article <https://support.emnify.com/hc/en-us/articles/4401906757906-How-to-configure-the-APN-on-different-devices>`_.
* SIM Registration and assignment.
* Device Creation
* Error Handling

.. literalinclude:: ../examples/mass_sim_activation.py
   :language: python
   :caption: mass_sim_activation.py


Devices Management
~~~~~~

.. literalinclude:: ../examples/devices.py
   :language: python
   :caption: devices.py


Device Lifecycle Management
~~~~~~

Create and activate a device
**************************


.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at: Create and activate a device
   :end-before: [endblock]


Configure a device
**************************


.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at:  Configure a device 
   :end-before: [endblock]


Configure operator blacklist for device
**************************


.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at:  Configure operator blacklist for device 
   :end-before: [endblock]


Disable device
**************************


.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at:  Disable device 
   :end-before: [endblock]


Delete device
**************************


.. literalinclude:: ../examples/device_lifecycle_management.py
   :language: python
   :caption: device_lifecycle_management.py
   :start-at:  Delete device 
   :end-before: [endblock]


