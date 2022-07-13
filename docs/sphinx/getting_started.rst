Getting Started
==========

Install
-------

Requirements
~~~~~~~~~~~~
Python > 3.6 is required.

Install From Source Code
~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash
   :caption: Installation commands

   git clone https://github.com/emnify-python-sdk.git
   cd emnify-python-sdk
   python setup.py install

Install via PyPi
~~~~~~~~~~~~~~~~
.. code-block:: bash
   :caption: Installation commands

   pip install emnify-sdk

Configure
---------

Create Application Token
~~~~~~~~~~~~~~~~~~~~~~~~

In order to use SDK you gonna need to create your Application Token via: `Enterprise Portal(Simplest Way) or API <https://www.emnify.com/developer-blog/how-to-use-an-application-token-for-api-authentication>`_ or , and apply it to initiate SDK.

Use in Code
~~~~~~~~~~~
.. literalinclude:: ../examples/first_operation.py
   :language: python
   :caption: Example of Usage
   :linenos:

Explore More
------------
Now when you have SDK configured it's time to learn what you can do further.

If you're new to IoT Connectivity and EMnify it makes sense to start with learning :doc:`concepts`. Visit our `Developers Hub <https://www.emnify.com/developers/documentation>`_ to learn more.

Once you're comfortable with :doc:`concepts` you may explore use-cases SDK is capable for, see :doc:`examples`.

The EMnify System Documentation can be found `here <https://cdn.emnify.net/api/doc/index.html>`_, the OpenAPI Documentation can be found `here <https://cdn.emnify.net/api/doc/swagger.html>`_.
