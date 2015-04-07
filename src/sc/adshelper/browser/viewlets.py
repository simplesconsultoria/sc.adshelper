# -*- coding: utf-8 -*-
"""
"""
from plone.app.layout.viewlets.common import ViewletBase
from plone import api


class HeadViewlet(ViewletBase):

    """Viewlet to be rendered inside the head tag."""

    def render(self):
        """Return the content of the head record."""
        return api.portal.get_registry_record('sc.adshelper.head')
