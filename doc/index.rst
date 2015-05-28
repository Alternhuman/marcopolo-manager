MarcoManager
============

MarcoManager is the central tool for automatization of services configuration through a set of extendable data structures.


It is designed to be used with MarcoPolo, however, it can easily be used as an (although not so powerful) alternative for *cron* or any other scheduling tool.

The system is built upon the definition of *services*, data structures which describe which actions are to be done, when and how frequently. The definition is loosely inspired in the Django ORM syntax.

MarcoManager runs as a daemon (both on systemd- and SysV-based systems) and it is built upon the Tornado ioloop.

