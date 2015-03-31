# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implements

PROJECTNAME = 'sc.adshelper'


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [
            u'sc.adshelper:uninstall',
            u'sc.adshelper.upgrades.v1010:default'
        ]
