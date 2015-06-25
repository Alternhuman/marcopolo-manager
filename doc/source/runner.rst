Runner
======

The runner class implements an IOLoop :class:`IOLoop<tornado.ioloop.IOLoop>` instance which runs all the :py:meth:`onSetup<marcomanager.marcomanager.MarcoManager.onSetup>` jobs on loading and schedules the :py:meth:`onReload<marcomanager.marcomanager.MarcoManager.onReload>` functionality accordingly.

By default, the runner loads all the :class:`MarcoManager<marcomanager.marcomanager.MarcoManager>`-inherited classes defined in the file `managers.py`. To include other file, just import it in the runner.py file.

The runner uses standard UNIX signals to reload the system and gracefully stopping all the managers using *SIGUSR1* to schedule functionality.


.. automodule:: marcomanager.runner
    :members:
    :undoc-members:
    