# -*- coding: utf-8 -*-
"""Viewlets used on the package."""
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from sc.adshelper.config import BASE_REGISTRY


class HtmlHeadViewlet(ViewletBase):

    """Viewlet to be rendered inside the head tag."""

    def render(self):
        """Return the content of the html_head record."""
        return api.portal.get_registry_record(BASE_REGISTRY + 'html_head')


class FooterViewlet(ViewletBase):

    """Viewlet to be rendered at the end of the document."""

    def render(self):
        """Return the content of the footer record."""
        return api.portal.get_registry_record(BASE_REGISTRY + 'footer')
