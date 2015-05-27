from abc import ABCMeta, abstractmethod
from tornado.concurrent import return_future
from concurrent.futures import ThreadPoolExecutor
class MarcoManager(object):
	__metaclass__ = ABCMeta
	def __init__(self):
		self.executor = ThreadPoolExecutor(max_workers=4)
	@abstractmethod
	def onSetup(self):
		pass

	@abstractmethod
	def onStop(self):
		pass

	def delay(self):
		return 0

	def onReload(self):
		pass
	
	def doReload(self):
		return False