Getting Started
==========

Install
-------

Requirements
~~~~~~~~~~~~
Python > 3.6 is required.

Install From Source Code
~~~~~~~~~~~~~~~~~~~
.. code-block:: bash
   :caption: Installation commands

   git clone https://github.com//emnify-python-sdk.git
   cd emnify-python-sdk
   python setup.py install

```

Install via PyPi
~~~~~~~~~~~~~~~~
.. code-block:: bash
   :caption: Installation commands

   pip install emnify-python-sdk

Configure
---------

Create Application Token
~~~~~~~~~~~~~~~~~~~~~~~~

Create your application token on: [https://portal.emnify.com/integrations/](https://portal.emnify.com/integrations/), and copy it.

Use in Code
~~~~~~~~~~~
.. code-block:: python
   :caption: Example of usage

   TOKEN = 'test'

   # 1) import package
   from emnify import EMnify

   # 2) initiate SDK instance using application token

   emnify = EMnify(TOKEN)

   # 3) Execute a command against desired API
   devices = emnify.devices.get_devices_list()


Explore More
~~~~~~~~~~~
