import sys, os
sys.path.append("/opt/marcopolo/")

from marcomanager import MarcoManager
from bindings.marco import marco
from tornado import gen
import time
from tornado.concurrent import Future, run_on_executor
class CompilerDiscover(MarcoManager):
	
	#@gen.coroutine
	@run_on_executor
	def onSetup(self):
		print("Hola")
		for i in range(0, 2):
			time.sleep(1)
			print(i)
		m = marco.Marco()
		nodes = m.request_for("compiler")
		f = open('/etc/distcc/hosts', 'a')
		for node in nodes:
			f.write(node["Address"])

		f.close()
		return "Discover"
		#raise gen.Return(1)
	def onStop(self):
		pass

	def delay(self):
		return 5

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
		return 600


class DemoManager(MarcoManager):
	@run_on_executor
	def onSetup(self):
		print("Setup")
		for i in range(30, 32):
			time.sleep(1)
			print(i)

		return("Demo")

	def delay(self):
		return 5

	def onStop(self):
		print("Killing")
	def onReload(self):
		print("Reloading")
	def doReload(self):
		return False