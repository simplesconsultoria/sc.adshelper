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


class AboveContentViewlet(ViewletBase):

    """Viewlet to be rendered above the content of the page."""

    def render(self):
        """Return the content of the above_content record."""
        return api.portal.get_registry_record(BASE_REGISTRY + 'above_content')


class BelowContentViewlet(ViewletBase):

    """Viewlet to be rendered below the content of the page."""

    def render(self):
        """Return the content of the below_content record."""
        return api.portal.get_registry_record(BASE_REGISTRY + 'below_content')


class FooterViewlet(ViewletBase):

    """Viewlet to be rendered at the end of the page."""

    def render(self):
        """Return the content of the footer record."""
        return api.portal.get_registry_record(BASE_REGISTRY + 'footer')
