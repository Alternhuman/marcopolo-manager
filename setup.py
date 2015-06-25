#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
import os
from distutils.core import setup
from distutils.command.clean import clean
from distutils.command.install import install
import os, sys
import subprocess

custom_marcomanager_params = [
                            "--marcomanager-disable-daemons",
                             ]

def detect_init():
    try:
        subprocess.check_call(["systemctl", "--version"], stdout=None, stderr=None, shell=False)
        return 0
    except (subprocess.CalledProcessError, OSError):
        return 1

init_bin = detect_init()

def enable_service(service):
    sys.stdout.write("Enabling service " + service +"...")
    if init_bin == 0:
        subprocess.call(["systemctl", "enable", service], shell=False)
    else:
        subprocess.call(["update-rc.d", "-f", service, "remove"], shell=False)
        subprocess.call(["update-rc.d", service, "defaults"], shell=False)
    
    sys.stdout.write("Enabled!")

def start_service(service):
    sys.stdout.write("Starting service " + service + "...")
    if init_bin == 0:
        subprocess.call(["systemctl", "start", service], shell=False)
    else:
        subprocess.call(["service", service, "start"], shell=False)

    sys.stdout.write("Started!")

if __name__ == "__main__":
    
    marcomanager_params = [param for param in sys.argv if param in custom_marcomanager_params]
    
    sys.argv = list(set(sys.argv) - set(marcomanager_params))

    python_version = int(sys.version[0])

    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as description_f:
        long_description = description_f.read()

    data_files = [
                  ('/etc/marcomanager/', [os.path.join(here, "etc/marcomanager/__init__.py")]),
                  ('/etc/marcomanager/managers/', [os.path.join(here, "etc/marcomanager/managers/managers.py"),
                                                   os.path.join(here, "etc/marcomanager/managers/__init__.py")])
                 ]

    if "--marcomanager-disable-daemons" not in marcomanager_params:
        

        if init_bin == 1:
            daemon_files = [
                         ('/etc/init.d/', ["daemons/systemv/marcomanagerd"])
                       ]
        else:
            daemon_files = [('/etc/systemd/system/',["daemons/systemd/marcomanager.service"])]

        data_files.extend(daemon_files)

    
    setup(
        name="marcomanager",
        provides=["marcomanager"],
        version='0.0.1',
        description="A task scheduler with MarcoPolo integration",
        long_description=long_description,
        url="marcopolo.martinarroyo.net",
        author="Diego Martín",
        author_email='martinarroyo@usal.es',
        license="MIT",
        classifiers=[
            'Development Status :: 3 - Alpha',

            'Intended Audience :: Developers',

            'Topic :: Software Development :: Build Tools',

            'License :: OSI Approved :: MIT License',

            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',

        ],

        keywords="marcomanager task scheduler",
        packages=find_packages(),
        install_requires=["marcopolo",
                          "tornado==4.1",
                          "futures",
                          "certifi==2015.4.28"],
        zip_safe=False,
        data_files=data_files,
        entry_points={
            'console_scripts':["marcomanagerd = marcomanager.runner:main",
                                "marcomanagerreload = marcomanager.marcomanagerreload:main"
                              ]
        }
    )
    
    if "--marcomanager-disable-daemons" not in marcomanager_params:
        enable_service("marcomanagerd")
        start_service("marcomanagerd")