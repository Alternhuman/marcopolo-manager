Examples of managers
====================

The managers are defined as a Python class which inherits from :class:`MarcoManager<marcomanager.marcomanager.MarcoManager>`. 

.. code-block:: python
	:caption: An example of a Manager
	:name: managers.py

	class DemoManager(MarcoManager):
		
		__disable__ = True # Set to true if the service is not to be included
		
		@run_on_executor
		def onSetup(self):
			"""
			Actions to include on setup
			"""
			nodes = marco.request_for("service")
			for node in nodes:
				do_something_with_node(node)

		def delay(self):
			"""
			Returns delay in seconds after startup.
			"""
			return 5

		def onStop(self):
			"""
			Actions to be executed befor stopping
			"""
			print("Killing")
		
		def onReload(self):
			"""
			Actions when the reload event is fired
			"""
			nodes = marco.request_for("service")
			for node in nodes:
				do_something_with_node(node)
		
		def doReload(self):
			"""
			Periodical reload interval
			"""
			return 0
.. 
	literalinclude:: ../../managers.py
	:language: python
	:emphasize-lines: 12,15-18
	:linenos:


Here are several examples:

.. automodule:: managers
	:members:
	:show-inheritance: