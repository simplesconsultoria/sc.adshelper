# -*- coding: utf-8 -*-
"""Viewlets used on the package."""
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from sc.adshelper.config import BASE_REGISTRY


class AdsHelperViewletBase(ViewletBase):

    """Base class for Ads Helper viewlets."""

    def show(self):
        """Return True if the viewlet will be visible.

        Viewlets will be visible for anonymous users only, unless
        we define in the control panel configlet that authenticated
        users will also see the code.

        As a security measure, viewlets are never shown in the context
        of the configlet. This way we can revert the inclusion of any
        code that breaks the layout.
        """
        context_state = api.content.get_view(
            u'plone_context_state', self.context, self.request)
        is_configlet = '@@adshelper-settings' in context_state.current_page_url()
        return not is_configlet and api.user.is_anonymous() or self.show_authenticated


class HtmlHeadViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered inside the head tag."""

    def update(self):
        """Update viewlet with the content of the html_head record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'html_head')


class HeaderViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered at the top of the page."""

    def update(self):
        """Update viewlet with the content of the header record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'header')


class AboveContentViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered above the content of the page."""

    def update(self):
        """Update viewlet with the content of the above_content record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'above_content')


class BelowContentViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered below the content of the page."""

    def update(self):
        """Update viewlet with the content of the below_content record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'below_content')


class BelowContentBodyViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered below the body of the content of the page."""

    def update(self):
        """Update viewlet with the content of the below_content record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'below_content_body')


class FooterViewlet(AdsHelperViewletBase):

    """Viewlet to be rendered at the end of the page."""

    def update(self):
        """Update viewlet with the content of the footer record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = api.portal.get_registry_record(BASE_REGISTRY + 'footer')
