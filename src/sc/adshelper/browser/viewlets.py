# -*- coding: utf-8 -*-
"""Viewlets used on the package."""
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from sc.adshelper.config import BASE_REGISTRY


class AdsHelperViewletBase(ViewletBase):

    """Base class for Ads Helper viewlets."""

    def show(self):
        return api.user.is_anonymous()


class HtmlHeadViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered inside the head tag."""

    def update(self):
        """Update viewlet with the content of the html_head record."""
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'html_head')


class AboveContentViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered above the content of the page."""

    def update(self):
        """Update viewlet with the content of the above_content record."""
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'above_content')


class BelowContentViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered below the content of the page."""

    def update(self):
        """Update viewlet with the content of the below_content record."""
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'below_content')


class FooterViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered at the end of the page."""

    def update(self):
        """Update viewlet with the content of the footer record."""
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'footer')
