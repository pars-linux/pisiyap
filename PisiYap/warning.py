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

from PyQt4 import QtCore, QtGui, Qt
from gui.warningui import Ui_Warning

class WarningWindow(QtGui.QDialog):
    def __init__(self,parent = None,modal = 0,fl = 0):
        QtGui.QDialog.__init__(self, parent)
        self.files = None
        self.ui = Ui_Warning()
        self.ui.setupUi(self)
