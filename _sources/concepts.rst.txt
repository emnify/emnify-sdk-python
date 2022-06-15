Concepts
========

.. list-table:: SDK Glossary
   :widths: 5 10
   :header-rows: 1

   * - Name
     - Description
   * - Device
     - Represents any physical device that can be supplied
       with a ``SIM`` and obtain connectivity.
       Don't mix up ``Device`` and ``Endpoint``,
       the difference is ``Device`` is a superset of ``Endpoint`` and ``SIM`` acting as whole.
       https://support.emnify.com/hc/en-us/sections/115000981005-Device-Configuration
   * - Device Status
     - Use it as your primary way to control connectivity.
       It can be either ``Enabled`` or ``Disabled``.
       When ``Enabled`` a ``Device`` that has a ``SIM`` assigned is getting online.
       On other hand when ``Disabled``, ``Device`` does not get any service.
   * - SIM
     - Represents a physical or eSIM that is issued by EMnify. https://support.emnify.com/hc/en-us/sections/360000642374-SIM-cards
   * - SIM Status
     - Status of the ``SIM`` represents SIM lifecycle https://www.emnify.com/blog/sim-lifecycle-management . Using SDK preffer not to change SIM status directly but rather via changing device status.
   * - Tariff Profile
     - Controls where and how your devices have coverage.
       https://cdn.emnify.net/api/doc/tariff-profile.html
       In Enterprise Portal it's referenced as ``Coverage Policy``.
   * - Service Profile
     - Defines available services(e.g. SMS, 4g...) and traffic limits for a device.
       https://cdn.emnify.net/api/doc/service-profile.html
       In Enterprise Portal it's referenced as ``Service Policy``.
   * - Blacklist Operators
     - Is a method that allows you to restrict connectivity of
       a ``Device`` to a specific ``Operator`` or a group of Operators.
   * - Operator
     - Represents an underlying mobile network operator that is used to provide you with connectivity.
       You can explore operators coverage by countries and regions here: https://www.emnify.com/pricing
   * - SMS
     - Learn https://www.emnify.com/developers/documentation#_sms
   * - Application Token
     - Your identity to use EMnify SDK and API.

`Complete Developer Glossary <https://www.emnify.com/developers/documentation#_glossary>`_ in Developer Hub.
