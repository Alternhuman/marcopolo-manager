from __future__ import absolute_import
from abc import ABCMeta, abstractmethod
from tornado.concurrent import return_future
from concurrent.futures import ThreadPoolExecutor

class MarcoManager(object):
	__metaclass__ = ABCMeta
	
	__disable__ = False
	
	def __init__(self):
		self.executor = ThreadPoolExecutor(max_workers=1)
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
		return 0