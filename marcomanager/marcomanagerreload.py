#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, signal, sys

def main(argv=None):
    PIDFILE='/var/run/marcomanager.pid'

    try:
        f = open (PIDFILE, 'r')
        pid = f.read()
        f.close()
        os.kill(int(pid), signal.SIGUSR1)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main(sys.argv[1:])