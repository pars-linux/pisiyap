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

from distutils.core import setup
from os import listdir, system

langs = []
for l in listdir('lang'):
    if l.endswith('ts'):
        system('lrelease lang/%s' % l)
        langs.append(('lang/%s' % l).replace('.ts', '.qm'))

datas = [('share/kde4/services/ServiceMenus', ['menu/PisiYap-kde4.desktop']),\
         ('share/applications', ['menu/PiSiYap.desktop']),\
         ('share/icons/hicolor/scalable/apps', ['icons/pisiyap.svg']),\
         ('lib/python2.7/site-packages/PisiYap/lang', langs),\
         ('share/pixmaps',      ['icons/pisiyap.png'])]

setup(name = "PiSiYap",
      version = "0.2",
      description = "PiSi Source Files Creator.",
      author = "Anıl Özbek",
      author_email = "ozbekanil@gmail.com",
      url = "https://code.google.com/p/pisiyap",
      packages = ["PisiYap", "PisiYap/templates", "PisiYap/gui"],
      data_files = datas,
      scripts = ['pisiyap']
      )
