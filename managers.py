from __future__ import absolute_import
import sys
sys.path.append("/opt/marcopolo/")

from tornado.concurrent import Future, run_on_executor

from bindings.marco import marco
from bindings.polo import polo

from marcomanager import MarcoManager

class CompilerDiscover(MarcoManager):
	"""
	Uses `MarcoPolo <file:///home/martin/TFG/workspaces/discovery/doc/build/html/index.html>`_ 
	through the  :class:`Marco python binding<bindings.marco.marco.Marco>` to
	discover the available `distcc <https://code.google.com/p/distcc/>`_ compilers on the network.
	If successful, it modifies the `/etc/distcc/hosts` with the results.

	This manager is executed with a delay of 10 seconds after startup and reloads every hour.
	"""
	@run_on_executor
	def onSetup(self):
		"""
		Sends a :py:meth:`Request_for<bindings.marco.marco.Marco.request_for>` message asking for nodes
		with the *compiler* service. If successful, it dumps the results to the '/etc/distcc/hosts file'
		"""
		m = marco.Marco()
		nodes = m.request_for("compiler")
		f = open('/etc/distcc/hosts', 'a')
		for node in nodes:
			f.write(node["Address"])

		f.close()
		return 0
		#TODO: Use DISTCC_HOME
	
	def onStop(self):
		"""
		Nothing is done
		"""
		pass

	def delay(self):
		"""
		Returns 10, the number of seconds to wait
		"""
		return 10

	def onReload(self):
		"""
		On reload, requests again for the *compiler* service, and dumps
		the results to the hosts file.
		"""
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
		"""
		Schedules a reload every 3600 seconds (an hour)
		"""
		return 3600

class HostnameManager(MarcoManager):
	"""
	Includes hostname information in marcopolo
	"""

	"""By default, disabled"""
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

