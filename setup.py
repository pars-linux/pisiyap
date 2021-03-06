# -*- coding: utf-8 -*-
#
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the docs/COPYING file.
#

from distutils.core import setup
from os import listdir, system
import glob

langs = []
for l in listdir('lang'):
    if l.endswith('ts'):
        system('lrelease lang/%s' % l)
        langs.append(('lang/%s' % l).replace('.ts', '.qm'))

datas = [('share/kde4/services/ServiceMenus', glob.glob('servicemenu/*.desktop')),\
         ('share/applications', ['menu/PiSiYaP.desktop']),\
         ('share/icons/hicolor/scalable/apps', ['icons/pisiyap.svg']),\
         ('lib/python2.7/site-packages/PisiYap/lang', langs)]

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
