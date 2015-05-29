#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, signal
PIDFILE='/var/run/marcopolo/marcomanager.pid'

try:
	f = open (PIDFILE, 'r')
	pid = f.read()
	f.close()
	os.kill(int(pid), signal.SIGUSR1)
except FileNotFoundError as e:
	print(e)
