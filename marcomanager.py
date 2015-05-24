#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
import tornado.ioloop
import signal
import sys
sys.path.append("/opt/marcopolo")
from bindings.polo import polo
from bindings.marco import marco

class MarcoManager(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def onSetup(self):
		pass

	@abstractmethod
	def onStop(self):
		pass

	
	def onReload(self):
		pass

	
	def doReload(self):
		return False

class CompilerDiscover(MarcoManager):
	def onSetup(self):
		marco = marco.Marco()
		nodes = marco.request_for("compiler")
		f = open('/etc/distcc/hosts', 'a')
		for node in nodes:
			f.write(node["Address"])

		f.close()
	def onStop(self):
		pass

	def onReload(self):
		marco = marco.Marco()
		nodes = marco.request_for("compiler")
		f = open('/etc/distcc/hosts', 'w')
		for node in nodes:
			f.write(node["Address"])
		f.close()

	def doReload(self):
		return 600	
class DemoManager(MarcoManager):
	def onSetup(self):
		print("Setup")
	def onStop(self):
		print("Killing")
	def onReload(self):
		print("Reloading")
	def doReload(self):
		return False
managers=None

def sigterm_handler(signum, frame):
	for manager in managers:
		manager.onStop()
	sys.exit(0)
def sigusr1_handler(signum, frame):
	signal.signal(signal.SIGUSR1, signal.SIG_IGN)
	for manager in managers:
		manager.onReload()
	signal.signal(signal.SIGUSR1, sigusr1_handler)

if __name__ == "__main__":
	signal.signal(signal.SIGTERM, sigterm_handler)
	signal.signal(signal.SIGUSR1, sigusr1_handler)
	signal.signal(signal.SIGINT, sigterm_handler)

	managers = [DemoManager()]

	io_loop = tornado.ioloop.IOLoop.instance()
	for manager in managers:
		manager.onSetup()
		r = manager.doReload()
		if r is not False:
			tornado.ioloop.PeriodicCallback(manager.onReload, r).start()

	io_loop.start()
