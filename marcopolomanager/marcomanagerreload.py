#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, signal, sys
from marcopolomanager import conf

def main(argv=None):
    PIDFILE=os.path.join(conf.RUNDIR, conf.PIDFILE)

    try:
        f = open (PIDFILE, 'r')
        pid = f.read()
        f.close()
        os.kill(int(pid), signal.SIGUSR1)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main(sys.argv[1:])