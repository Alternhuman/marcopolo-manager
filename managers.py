from __future__ import absolute_import
import sys
sys.path.append("/opt/marcopolo/")

from tornado.concurrent import Future, run_on_executor

from bindings.marco import marco
from bindings.polo import polo

from marcomanager import MarcoManager

class CompilerDiscover(MarcoManager):
	
	@run_on_executor
	def onSetup(self):
		m = marco.Marco()
		nodes = m.request_for("compiler")
		f = open('/etc/distcc/hosts', 'a')
		for node in nodes:
			f.write(node["Address"])

		f.close()
		return 0
	
	def onStop(self):
		pass

	def delay(self):
		return 10

	def onReload(self):
		m = marco.Marco()
		nodes = m.request_for("compiler")
		try:
			f = open('/etc/distcc/hosts', 'w')
			for node in nodes:
				f.write(node["Address"])
			f.close()
		except FileNotFoundException:
			pass
	
	def doReload(self):
		return 3600

class HostnameManager(MarcoManager):
	__disable__ = True
	@run_on_executor
	def onSetup(self):
		import socket
		hostname = socket.gethostname()

	def onStop(self):
		pass

	def onReload(self):
		import socket
		hostname = socket.gethostname()

	def doReload(self):
		return 3600

class EnableTomcatManager(MarcoManager):
	@run_on_executor
	def onSetup(self):
		pass

	def onStop(self):
		pass

class EnableHadoopMaster(MarcoManager):
	@run_on_executor
	def onSetup(self):
		pass

	def onStop(self):
		pass

class DemoManager(MarcoManager):
	__disable__ = True
	@run_on_executor
	def onSetup(self):
		return 1

	def delay(self):
		return 5

	def onStop(self):
		print("Killing")
	def onReload(self):
		print("Reloading")
	def doReload(self):
		return 0