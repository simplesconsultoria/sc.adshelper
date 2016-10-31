# -*- coding: utf-8 -*-
from collective.blueline import _
from lxml import etree
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.formlib import form
from zope.interface import implementer
from zope.schema import ValidationError


class InvalidHTMLCode(ValidationError):

    """The code is not valid."""


def validateHTMLCode(code):
    """Validate code inserted into portlet."""
    if code:
        parser = etree.HTMLParser(recover=False)
        try:
            etree.HTML(code, parser)
        except etree.XMLSyntaxError:
            raise InvalidHTMLCode
    return True


class IBluelinePortlet(IPortletDataProvider):

    """Blueline Portlet."""

    embed = schema.Text(
        title=_(u'Embedding code'),
        required=False,
        constraint=validateHTMLCode,
    )

    title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )


@implementer(IBluelinePortlet)
class Assignment(base.Assignment):

    embed = None
    title = None
    description = None

    def __init__(self, embed=None, title=None, description=None):
        self.embed = embed
        self.title = title
        self.description = description


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('blueline.pt')


class AddForm(base.AddForm):

    form_fields = form.Fields(IBluelinePortlet)
    label = _(u'Add Blueline Portlet')
    description = _(u'This portlet embeds content from remote source.')

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):

    form_fields = form.Fields(IBluelinePortlet)
    label = _(u'Edit Blueline Portlet')
    description = _(u'This portlet embeds content from remote source.')
