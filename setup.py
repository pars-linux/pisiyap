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
        system('lrelease-qt4 lang/%s' % l)
        langs.append(('lang/%s' % l).replace('.ts', '.qm'))

datas = [('kde/3.5/share/apps/konqueror/servicemenus', ['menu/PisiYap-kde3.desktop']),\
         ('kde/4/share/kde4/services/ServiceMenus', ['menu/PisiYap-kde4.desktop']),\
         ('share/applications', ['menu/PisiYap.desktop']),\
         ('share/icons/hicolor/scalable/apps', ['icons/pisiyap.svg']),\
         ('lib/python2.5/site-packages/PisiYap/lang', langs),\
         ('share/pixmaps',      ['icons/pisiyap.png'])]

setup(name = "PisiPap",
      version = "0.1",
      description = "PiSi Source Files Creator.",
      author = "Murat Şenel",
      author_email = "muratasenel@gmail.com",
      url = "http://www.muratsenel.net/pisiyap",
      packages = ["PisiYap", "PisiYap/templates", "PisiYap/gui"],
      data_files = datas,
      scripts = ['pisiyap']
      )
