class MarcoManager(object):
	"""
	Abstract class which defines all the available functionality.
	Some methods are concrete, since they have a default 
	action only executed if not overriden.
	"""
	__metaclass__ = ABCMeta

	@abstractmethod
	def onSetup(self):
		"""
		Actions to be executed only during startup.
		The code is run asynchronously in a different thread than
		the main code, so it is safe to execute blocking actions 			without blocking the whole IOLoop.
		The method is called immediately after the daemon is started
		or when the specified delay is passed.
		"""
		pass

	@abstractmethod
	def onStop(self):

		"""
		Actions to be executed before the daemon is terminated
		The method runs asynchronously in a different thread, just like
		onSetup(), so it allows blocking behaviour.
		"""
		pass

	
	def onReload(self):
		"""
		Actions to be executed when the reload signal is received.
		Runs asynchronously.
		"""
		pass

	
	def doReload(self):

		"""
		Indicates whether the manager has reloading funcionality.
		By default it returns false.
		"""

		return False
	def delay(self):
		"""
		Indicates the delay (in seconds) to wait before executing the onSetup() function.
		By default it returns 0
 		"""
