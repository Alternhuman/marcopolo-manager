Installation
============

The installation of the package is quite simple and can be accomplished with very little or any manual configuration.

pip
---

Issuing the following command will install all the required files:

::

	pip install marcomanager

setuptools
----------

Alternatively it is possible to download the full package from the repository or pip and install it using the following command:

::
	
	python setup.py install

Please note that root access may be necessary depending on your setup.

The script installs the following files:

- The package ``marcomanager`` in the default Python library directory.
- An entry point called ``marcomanagerd``
- A service file in the ``/etc/init.d`` or ``/etc/systemd/system/`` directory.
- Some configuration files in ``/etc/marcomanager``
 
The installation script enables the service by default (with no services). You can create services and then ``reload`` the service. Please note that the Marco or Polo daemons must be running in order to use them, and will not be enabled by the service.