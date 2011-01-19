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

pspecXml = u'''<?xml version="1.0" ?>
<!DOCTYPE PISI SYSTEM "http://www.pardus.org.tr/projeler/pisi/pisi-spec.dtd">
<PISI>
    <Source>
        <Name>%(packageName)s</Name>
        <Homepage>%(homePage)s</Homepage>
        <Packager>
            <Name>%(packagerName)s</Name>
            <Email>%(packagerEmail)s</Email>
        </Packager>
        <License>%(license)s</License>%(icon)s
        <IsA>%(isA)s</IsA>
        <Summary>%(summary)s</Summary>
        <Description>%(description)s</Description>
        <Archive sha1sum="%(sha1Sum)s" type="%(archiveType)s">%(archiveAddr)s</Archive>
        <!--
        <BuildDependencies>
            <Dependency>Dep1-devel</Dependency>
            <Dependency>Dep2-devel</Dependency>
            <Dependency>Dep3-devel</Dependency>
            <Dependency versionFrom="">Dep4-devel</Dependency>
        </BuildDependencies>
        -->
        <!--
        <Patches>
            <Patch>%(packageName)s.patch</Patch>
            <Patch level="1">%(packageName)s.patch</Patch>
        </Patches>
        -->
    </Source>

    <Package>
        <Name>%(packageName)s</Name>
        <!--
        <RuntimeDependencies>
            <Dependency>Dep1</Dependency>
            <Dependency>Dep2</Dependency>
            <Dependency>Dep3</Dependency>
            <Dependency versionFrom="">Dep4</Dependency>
        </RuntimeDependencies>
        -->
        <Files>
            <Path fileType="all">/</Path>
            <!--
            <Path fileType="executable">/usr/bin</Path>
            <Path fileType="config">/etc</Path>
            <Path fileType="library">/usr/lib</Path>
            <Path fileType="header">/usr/include</Path>
            <Path fileType="data">/usr/share</Path>
            <Path fileType="localedata">/usr/share/locale</Path>
            <Path fileType="man">/usr/share/man</Path>
            <Path fileType="info">/usr/share/info</Path>
            <Path fileType="doc">/usr/share/doc</Path>
            -->
        </Files>
        <!--
        <AdditionalFiles>
            <AdditionalFile owner="root" permission="0644" target="/usr/share/applications/%(packageName)s.desktop">%(packageName)s.desktop</AdditionalFile>
            <AdditionalFile owner="root" permission="0644" target="/usr/share/pixmaps/%(packageName)s.png">%(packageName)s.png</AdditionalFile>
        </AdditionalFiles>
        -->
        <!--
        <Provides>
            <COMAR script="package.py">System.Package</COMAR>
            <COMAR script="service.py">System.Service</COMAR>
        </Provides>
        -->
    </Package>

    <History>
        <Update release="1">
            <Date>%(date)s</Date>
            <Version>%(pkgVersion)s</Version>
            <Comment>First release</Comment>
            <Name>%(packagerName)s</Name>
            <Email>%(packagerEmail)s</Email>
        </Update>
    </History>
</PISI>
'''
