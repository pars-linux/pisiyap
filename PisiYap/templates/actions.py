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

autoTools = u'''#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
'''

cmakeTools = u'''#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
'''

kdeTools = u'''#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
'''

perlTools = u'''#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
'''

pyTools = u'''#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
'''

sconsTools = u'''#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools

def setup():
    scons.configure()

def build():
    scons.make()

def install():
    scons.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
'''
