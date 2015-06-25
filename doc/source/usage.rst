Usage
=====

In order to include functionality to the manager, a management unit must be created. Those are stored in the ``/etc/marcomanager/managers/managers.py`` file.

A management unit is a python class that extends from the :class:`MarcoManager <marcomanager.marcomanager.Marcomanager>` class. By redefining the provided methods the behaviour of the unit is defined. The list of methods and its behaviour is defined in the :ref:`reference <marcomanagerreference>`.

daemon
------

The package is intented to be run as a system daemon, and works in both ``initd`` and ``systemd``. It can be reloaded, started, stopped... just as any other daemon:

::
    
    # Start service
    service marcomanagerd start
    systemctl start marcomanagerd


    # Stop service
    service marcomanagerd stop
    systemctl  stopmarcomanagerd

    # And so on...