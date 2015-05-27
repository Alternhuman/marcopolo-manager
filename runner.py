#!/usr/bin/env python3

import signal, conf, logging
import sys, os
import tornado.ioloop
from managers import *

from marcomanager import MarcoManager

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

import inspect

classes = []
managers = []

for name, obj in [(name, obj) for name, obj in inspect.getmembers(sys.modules[__name__]) if issubclass(obj.__class__, MarcoManager.__class__) and name not in ["Future", "ABCMeta", "MarcoManager"]]:
	print (name, obj)
	classes.append(obj)

if __name__ == "__main__":
	def f(t):
		print(t.result())
	
	for c in classes:
		managers.append(c())

	signal.signal(signal.SIGTERM, sigterm_handler)
	signal.signal(signal.SIGUSR1, sigusr1_handler)
	signal.signal(signal.SIGINT, sigterm_handler)
	signal.signal(signal.SIGHUP, signal.SIG_IGN)
	
	io_loop = tornado.ioloop.IOLoop.instance()
	for manager in managers:
		#io_loop.call_later(manager.delay(), io_loop.add_future, manager.onSetup)
		io_loop.add_future(manager.onSetup(), f)
		r = manager.doReload()
		if r is not False:
			tornado.ioloop.PeriodicCallback(manager.onReload, r).start()

	pid = os.getpid()
	if not os.path.exists(conf.RUNDIR):
		os.makedirs(conf.RUNDIR)

	f = open(os.path.join(conf.RUNDIR, conf.PIDFILE), 'w')
	f.write(str(pid))
	f.close()
	
	if not os.path.exists(conf.LOGDIR):
		os.makedirs(conf.LOGDIR)
	logging.basicConfig(filename=os.path.join(conf.LOGDIR, conf.LOGFILE), level=logging.DEBUG)	
	io_loop.start()
