# -*- coding: utf-8 -*-
#
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the docs/COPYING file.
#

comarScript = '''#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    pass
'''

serviceScript = '''#!/usr/bin/python

from comar.service import *

serviceType="server"
serviceDesc = _({"en": "%(packageName)s Server",
                 "tr": "%(packageName)s Sunucusu"})

@synchronized
def start():
    startService(command="/usr/bin/%(packageName)s",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/%(packageName)s.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/%(packageName)s.pid")
'''
