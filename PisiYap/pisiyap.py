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

from PyQt4 import QtCore, QtGui, Qt
from gui.pisiyapui import Ui_Pisiyap
from warning import WarningWindow
from finished import FinishDialog
from time import strftime
from subprocess import *
import os, sys

class PisiYap(QtGui.QMainWindow):
    def __init__(self,parent = None,modal = 0,fl = 0):
        QtGui.QMainWindow.__init__(self, None)
        self.ui = Ui_Pisiyap()
        self.warningWindow = WarningWindow(self)
        self.finishedDialog = FinishDialog(self)
        self.ui.setupUi(self)
        self.date = strftime('%Y-%m-%d')
        self.user = os.getenv('USER')
        self.configFile = os.path.join('/home/' + self.user, '.pisiyap')

        if len(sys.argv) > 1:
            self.ui.brwsLine_.setText(sys.argv[-1])

        if os.path.exists(self.configFile) and self.checkConfig() == False:
            self.ui.pisiyapTab.setCurrentIndex(0)
        elif os.path.exists(self.configFile):
                self.ui.pisiyapTab.setCurrentIndex(1)
                self.ui.pkgerName.setText(self.readConfig(0))
                self.ui.pkgerEmail.setText(self.readConfig(1))
                self.ui.brwsLine.setText(self.readConfig(2))
                self.ui.pkgerName_.setText(self.readConfig(0))
                self.ui.pkgerEmail_.setText(self.readConfig(1))

    def mkdir(self, directory):
        if not os.path.exists(directory):
            os.mkdir(directory)

    def nextAction(self):
        currentTab = self.ui.pisiyapTab.currentIndex()
        self.ui.pisiyapTab.setCurrentIndex(currentTab + 1)

    def backAction(self):
        currentTab = self.ui.pisiyapTab.currentIndex()
        self.ui.pisiyapTab.setCurrentIndex(currentTab - 1)

    def createConfig(self):
        packagerName = unicode(self.ui.pkgerName.text())
        packagerEmail = unicode(self.ui.pkgerEmail.text())
        config = [packagerName, packagerEmail, self.packageDir()]
        configFile = file(self.configFile, 'w')
        configFile.write('\n'.join(config))
        configFile.close()
        self.ui.pkgerName_.setText(self.readConfig(0))
        self.ui.pkgerEmail_.setText(self.readConfig(1))
        self.ui.pisiyapTab.setCurrentIndex(1)

        self.mkdir(self.packageDir())

    def checkConfig(self):
        config = open(self.configFile).readlines()
        if not len(config) == 3:
            return False

    def readConfig(self, int):
        config = open(self.configFile).readlines()
        return unicode(config[int].strip())

    def selectDir(self):
        directory = QtGui.QFileDialog.getExistingDirectory(None, self.trUtf8("Choose a directory to store PiSi packages"))
        self.ui.brwsLine.setText(directory)

    def packageDir(self):
        return str(self.ui.brwsLine.text())

    def brwSource(self):
        sourceFile = QtGui.QFileDialog.getOpenFileName(None, self.trUtf8("Select source file"), '', '', None)
        self.ui.brwsLine_.setText(sourceFile)
        self.copyArchive()

    def copyArchive(self):
        sourceFile = self.ui.brwsLine_.text()
        if sourceFile and self.ui.copyArchive.isChecked():
            Popen(['/usr/bin/xdg-su', '-u', 'root', '-c', '/bin/mkdir -p /var/cache/pisi/archives && /bin/cp "%s" /var/cache/pisi/archives/' % sourceFile])

    def homePage(self):
        homePage = str(self.ui.homePage.text())
        if homePage:
            return homePage
        else:
            return [False, self.trUtf8('Home Page')]

    def archiveAddr(self):
        archiveAddr = str(self.ui.archiveAddr.text())
        if archiveAddr:
            return archiveAddr
        else:
            return [False, self.trUtf8('Archive Address')]

    def pkgVersion(self):
        pkgVersion = str(self.ui.pkgVer.text())
        newPkgVersion = str(self.ui.newPkgVer.text())
        if pkgVersion and not newPkgVersion:
            return pkgVersion
        elif newPkgVersion:
            return newPkgVersion
        else:
            return [False, self.trUtf8('Package Version')]

    def fileName(self):
        fileName = str(self.ui.brwsLine_.text())
        if fileName:
            return fileName.split('/')[-1]
        else:
            return [False, self.trUtf8('Archive File')]

    def archiveType(self, int):
        filename = self.fileName()
        if filename.endswith('bz2'):
            archivetype = 'tarbz2'
            extension = '.tar.bz2'
        elif filename.endswith('gz'):
            archivetype = 'targz'
            extension = '.tar.gz'
        elif filename.endswith('tgz'):
            archivetype = 'targz'
            extension = '.tgz'
        elif filename.endswith('zip'):
            archivetype = 'zip'
            extension = '.zip'
        elif filename.endswith('rar'):
            archivetype = 'rar'
            extension = '.rar'
        else:
            archivetype = 'binary'
            extension = False
        list = [archivetype, extension]
        return list[int]

    def packageName(self):
        if self.fileName()[0]:
            name = self.fileName().split('-')[0].split(".")[0]
            self.ui.pkgName.setText(name)
            package = str(self.ui.pkgName.text())
            newPackage = str(self.ui.newPkgName.text())
            if package and not newPackage:
                packageName = package
            elif newPackage:
                packageName = newPackage
            if self.archiveType(1) != False:
                version = self.fileName().split('-')[-1].split(self.archiveType(1))[0]
                self.ui.pkgVer.setText(version)
        else:
            packageName = [False, self.trUtf8('Package Name')]

        return packageName

    def packagerName(self):
        packagerName = unicode(self.ui.pkgerName_.text())
        if packagerName:
            return packagerName
        else:
            return [False, self.trUtf8('Packager Name')]

    def packagerEmail(self):
        packagerEmail = unicode(self.ui.pkgerEmail_.text())
        if packagerEmail:
            return packagerEmail
        else:
            return [False, self.trUtf8('Packager E-mail')]

    def license(self):
        license = str(self.ui.license.currentText())
        newLicense = str(self.ui.newLicense.text())
        if license and not newLicense:
            return license
        elif newLicense:
            return newLicense
        else:
            return [False, self.trUtf8('License')]

    def isA(self):
        isA = str(self.ui.isA.currentText())
        if isA:
            return isA
        else:
            return [False, self.trUtf8('isA Tag')]

    def summary(self):
        summary = str(self.ui.summary.toPlainText())
        if summary:
            return summary
        else:
            return [False, self.trUtf8('Summary')]

    def description(self):
        description = str(self.ui.description.toPlainText())
        if description:
            return description
        else:
            return [False, self.trUtf8('Description')]

    def sha1Sum(self):
        sha1sum = Popen(['sha1sum', str(self.ui.brwsLine_.text())], stdout=PIPE).communicate()[0].split('\n')
        return sha1sum[0].strip().split(' ')[0]

    def checkDesktopFile(self):
        if self.isA() == 'app:gui':
            self.ui.desktopFile.setChecked(True)
            self.ui.iconTag.setChecked(True)
        else:
            self.ui.desktopFile.setChecked(False)
            self.ui.iconTag.setChecked(False)

    def checkIconTag(self):
        if self.ui.desktopFile.isChecked():
            self.ui.iconTag.setChecked(True)

    def iconTag(self):
        iconTag = '''\n        <Icon>%s</Icon>''' % self.packageName()
        if self.ui.iconTag.isChecked():
            return iconTag
        else:
            return ''

    def checkFields(self):
        emptyFields = []
        fields = [self.fileName(), self.homePage(), self.archiveAddr(), self.pkgVersion(), self.packageName(), self.packagerName(), 
                  self.packagerEmail(), self.license(), self.isA(), self.summary(), self.description()]
        for f in fields:
            if f[0] is False:
                emptyFields.append(unicode(f[1]))

        if len(emptyFields) > 0:
            empty_fields = ', '.join(emptyFields)
            self.warningWindow.ui.warnings.setText(empty_fields)
            self.warningWindow.show()

        if len(emptyFields) == 0:
            return True

    def createFiles(self):
        from templates import pspec, actions, desktop, translations, comar
        if self.checkFields():
            packageDir = os.path.join(self.readConfig(2), self.packageName())
            self.mkdir(packageDir)

            resources = {'packageName'   :  self.packageName(),
                         'homePage'      :  self.homePage(),
                         'packagerName'  :  self.packagerName(),
                         'packagerEmail' :  self.packagerEmail(),
                         'license'       :  self.license(),
                         'icon'          :  self.iconTag(),
                         'isA'           :  self.isA(),
                         'summary'       :  self.summary(),
                         'description'   :  self.description(),
                         'sha1Sum'       :  self.sha1Sum(),
                         'archiveType'   :  self.archiveType(0),
                         'archiveAddr'   :  self.archiveAddr(),
                         'date'          :  self.date,
                         'pkgVersion'    :  self.pkgVersion()}

            pspecXml = file(os.path.join(packageDir, 'pspec.xml'), 'w')
            pspecXml.write(pspec.pspecXml % resources)
            pspecXml.close()

            if self.ui.autoTools.isChecked():
                actionspy = actions.autoTools
            elif self.ui.cmakeTools.isChecked():
                actionspy = actions.cmakeTools
            elif self.ui.kde4Tools.isChecked():
                actionspy = actions.kde4Tools
            elif self.ui.qt4Tools.isChecked():
                actionspy = actions.qt4Tools
            elif self.ui.pyTools.isChecked():
                actionspy = actions.pyTools
            elif self.ui.sconsTools.isChecked():
                actionspy = actions.sconsTools

            actionsPy = file(os.path.join(packageDir, 'actions.py'), 'w')
            actionsPy.write(actionspy)
            actionsPy.close()

            translationsXml = file(os.path.join(packageDir, 'translations.xml'), 'w')
            translationsXml.write(translations.translationXml % resources)
            translationsXml.close()

            if self.ui.desktopFile.isChecked():
                desktopFilePath = os.path.join(packageDir, 'files')
                self.mkdir(desktopFilePath)
                desktopFile = file(os.path.join(desktopFilePath, self.packageName() + '.desktop'), 'w')
                desktopFile.write(desktop.desktopFile % resources)
                desktopFile.close()

            if self.ui.comarScript.isChecked():
                comarScriptPath = os.path.join(packageDir, 'comar')
                self.mkdir(comarScriptPath)
                comarScript = file(os.path.join(comarScriptPath, 'package.py'), 'w')
                comarScript.write(comar.comarScript % resources)
                comarScript.close()

            if self.ui.serviceScript.isChecked():
                serviceScriptPath = os.path.join(packageDir, 'comar')
                self.mkdir(comarScriptPath)
                serviceScript = file(os.path.join(serviceScriptPath, 'service.py'), 'w')
                serviceScript.write(comar.serviceScript % resources)
                serviceScript.close()

            if self.ui.openDirectory.isChecked():
                Popen(['/usr/bin/xdg-open', packageDir])
            else:
                self.finishedDialog.show()
