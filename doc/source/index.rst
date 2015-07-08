.. marcomanager documentation master file, created by
   sphinx-quickstart on Fri May 29 09:21:13 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to marcomanager's documentation!
========================================

MarcoManager
============

MarcoManager is the central tool for automatization of service configuration through a set of extendable data structures.

It is designed to integrate `MarcoPolo <marcopoloproject.martinarroyo.net/marcopolo>`_. It can however easily be used as an (although not so powerful) alternative for ``cron`` or any other scheduling tool.

The system is built upon the definition of *service units*, python classes which describe which actions are to be done, when and how frequently. This is loosely inspired in the Django ORM model definition strategy.

MarcoManager runs as a daemon (both on systemd- and SysV-based systems) and it is built upon the Tornado :class:`ioloop<tornado.ioloop.IOLoop>`.

Contents:

.. toctree::
    :maxdepth: 2

    installation
    managers
    usage
    The MarcoManager class <marcomanager>
    The Runner class <runner>
    software_engineering/intro


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

