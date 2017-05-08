# -*- coding: utf-8 -*-
"""Viewlets used on the package."""
from collective.blueline.config import BASE_REGISTRY
from os import path
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import tempfile


class BluelineViewletBase(ViewletBase):

    """Base class for Blueline viewlets."""

    def show(self):
        """Return True if the viewlet will be visible.

        Viewlets will be visible for anonymous users only, unless
        we define in the control panel configlet that authenticated
        users will also see the code.

        As a security measure, viewlets are never shown in the context
        of the configlet. This way we can revert the inclusion of any
        code that breaks the layout.

        Viewlets are neither shown in the Diazo configlet.
        """
        context_state = api.content.get_view(
            u'plone_context_state', self.context, self.request)
        void_configlets = ('@@blueline-settings', '@@theming-controlpanel')
        is_configlet = False
        for name in void_configlets:
            is_configlet |= name in context_state.current_page_url()
        show = api.user.is_anonymous() or self.show_authenticated
        return not is_configlet and show

    def get_template(self, name, data):
        """Evaluate TAL variables inserted into blueline controlpanel options.
        We need a temporary file with page template to evaluate variables using
        TAL machinary.

        :param name: name of blueline registry with code
        :type name: string
        :param data: data of blueline registry with code
        :type data: unicode
        :returns: page template ready to be evaluated
        :rtype: ViewPageTemplateFile
        """
        filename = 'collective.blueline.{0}.pt'.format(name)
        filename = path.join(tempfile.tempdir, filename)
        with open(filename, 'w') as f:
            f.write(data)
        return ViewPageTemplateFile(filename)

    def evaluate_code(self, name):
        """Evaluate TAL variables inserted into blueline controlpanel options.

        :param name: name of blueline registry with code
        :type name: string
        :returns: code with variables evaluated
        :rtype: unicode
        """
        data = api.portal.get_registry_record(BASE_REGISTRY + name)
        if data is None or data == '':
            return None
        template = self.get_template(name, data)
        return template(self)


class HtmlHeadViewlet(BluelineViewletBase):

    """Viewlet to be rendered inside the head tag."""

    def update(self):
        """Update viewlet with the content of the html_head record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = self.evaluate_code('html_head')


class HeaderViewlet(BluelineViewletBase):

    """Viewlet to be rendered at the top of the page."""

    def update(self):
        """Update viewlet with the content of the header record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = self.evaluate_code('header')


class AboveContentViewlet(BluelineViewletBase):

    """Viewlet to be rendered above the content of the page."""

    def update(self):
        """Update viewlet with the content of the above_content record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = self.evaluate_code('above_content')


class BelowContentViewlet(BluelineViewletBase):

    """Viewlet to be rendered below the content of the page."""

    def update(self):
        """Update viewlet with the content of the below_content record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = self.evaluate_code('below_content')


class BelowContentBodyViewlet(BluelineViewletBase):

    """Viewlet to be rendered below the body of the content of the page."""

    def update(self):
        """Update viewlet with the content of the below_content record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = self.evaluate_code('below_content_body')


class FooterViewlet(BluelineViewletBase):

    """Viewlet to be rendered at the end of the page."""

    def update(self):
        """Update viewlet with the content of the footer record."""
        self.show_authenticated = api.portal.get_registry_record(BASE_REGISTRY + 'show_authenticated')
        self.code = self.evaluate_code('footer')
