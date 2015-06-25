#!/usr/bin/env python

from __future__ import absolute_import
import signal, logging
import sys, os
import inspect

import tornado.ioloop
import tornado.concurrent

from marcomanager import conf
from marcomanager.marcomanager import MarcoManager

sys.path.insert(0, conf.MANAGERS_DIR)
from managers import *

io_loop = tornado.ioloop.IOLoop.instance()

def sigterm_handler(signum, frame):
    for manager in manager_instances:
        manager.onStop()
    logging.info("Stopping runner")
    io_loop.stop()
    sys.exit(0)

def sigusr1_handler(signum, frame):
    signal.signal(signal.SIGUSR1, signal.SIG_IGN)
    for manager in manager_instances:
        manager.onReload()
    logging.info("Reloading runner")
    signal.signal(signal.SIGUSR1, sigusr1_handler)


classes = []
manager_instances = []
names = []
for name, obj in [(name, obj) for name, obj in \
    inspect.getmembers(sys.modules[__name__]) \
    if issubclass(obj.__class__, MarcoManager.__class__) \
    and name not in ["Future", "ABCMeta", "MarcoManager"]]:
    classes.append(obj)
    names.append(name)



def log(future):
    result = future.result()
    if result is not None:
        logging.info(future.result())


def main(argv=None):  
    for manager_instance in [m for m in classes if m.__disable__ == False]:
        manager_instances.append(manager_instance())

    signal.signal(signal.SIGTERM, sigterm_handler)
    signal.signal(signal.SIGUSR1, sigusr1_handler)
    signal.signal(signal.SIGINT, sigterm_handler)
    #signal.signal(signal.SIGHUP, signal.SIG_IGN)
    
    for manager in manager_instances:
        if manager.enable():
            io_loop.call_later(manager.delay(), 
                               io_loop.add_future, 
                               manager.onSetup(), 
                               log)
            
            doReload = int(manager.doReload()) * 1000
            if doReload != False:
                tornado.ioloop.PeriodicCallback(manager.onReload, doReload).start()

    pid = os.getpid()
    if not os.path.exists(conf.RUNDIR):
        os.makedirs(conf.RUNDIR)

    f = open(os.path.join(conf.RUNDIR, conf.PIDFILE), 'w')
    f.write(str(pid))
    f.close()
    
    if not os.path.exists(conf.LOGDIR):
        os.makedirs(conf.LOGDIR)
    logging.basicConfig(filename=os.path.join(conf.LOGDIR, conf.LOGFILE),
                        level=logging.DEBUG)
    
    logging.info("Starting runner with the services %s" % u', '.join(names))
    
    io_loop.start()

if __name__ == "__main__":
    main(sys.argv[1:])
