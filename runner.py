#!/usr/bin/env python3

from __future__ import absolute_import
import signal, conf, logging
import sys, os
import inspect

import tornado.ioloop
import tornado.concurrent
from managers import *

from marcomanager import MarcoManager

def sigterm_handler(signum, frame):
    for manager in manager_instances:
        manager.onStop()
    logging.info(u"Stopping runner")
    io_loop.stop()
    sys.exit(0)

def sigusr1_handler(signum, frame):
    signal.signal(signal.SIGUSR1, signal.SIG_IGN)
    for manager in manager_instances:
        manager.onReload()
    logging.info(u"Reloading runner")
    signal.signal(signal.SIGUSR1, sigusr1_handler)


classes = []
manager_instances = []
names = []
for name, obj in [(name, obj) for name, obj in \
    inspect.getmembers(sys.modules[__name__]) \
    if issubclass(obj.__class__, MarcoManager.__class__) \
    and name not in [u"Future", u"ABCMeta", u"MarcoManager"]]:
    classes.append(obj)
    names.append(name)



def log(future):
    result = future.result()
    if result is not None:
        logging.info(future.result())

if __name__ == u"__main__":
    
    for c in [m for m in classes if m.__disable__ == False]:
        manager_instances.append(c())

    signal.signal(signal.SIGTERM, sigterm_handler)
    signal.signal(signal.SIGUSR1, sigusr1_handler)
    signal.signal(signal.SIGINT, sigterm_handler)
    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    
    io_loop = tornado.ioloop.IOLoop.instance()
    for manager in manager_instances:
        io_loop.call_later(manager.delay(), io_loop.add_future, manager.onSetup(), log)
        
        r = int(manager.doReload()) * 1000
        if r != False:
            tornado.ioloop.PeriodicCallback(manager.onReload, r).start()

    pid = os.getpid()
    if not os.path.exists(conf.RUNDIR):
        os.makedirs(conf.RUNDIR)

    f = open(os.path.join(conf.RUNDIR, conf.PIDFILE), 'w')
    f.write(str(pid))
    f.close()
    
    if not os.path.exists(conf.LOGDIR):
        os.makedirs(conf.LOGDIR)
    logging.basicConfig(filename=os.path.join(conf.LOGDIR, conf.LOGFILE),\
     level=logging.DEBUG)
    logging.info(u"Starting runner with the services %s" % u', '.join(names))
    io_loop.start()
