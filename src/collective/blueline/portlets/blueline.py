# -*- coding: utf-8 -*-
from collective.blueline import _
from collective.blueline.interfaces import validCodeConstraint
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.formlib import form
from zope.interface import implementer


class IBluelinePortlet(IPortletDataProvider):

    '''Blueline Portlet.'''

    embed = schema.Text(
        title=_(u'Embedding code'),
        required=False,
        constraint=validCodeConstraint,
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

    def __init__(self,
                 embed=None,
                 title=None,
                 description=None):
        self.embed = embed
        self.title = title
        self.description = description


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('blueline.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)


class AddForm(base.AddForm):

    form_fields = form.Fields(IBluelinePortlet)

    label = _(u'Add Blueline Portlet')
    description = _(u'blueline_portlet_description',
                    default=u'This portlet embed content from remote source.')

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):

    form_fields = form.Fields(IBluelinePortlet)

    label = _(u'Edit Blueline Portlet')
    description = _('blueline_portlet_description',
                    default=u'This portlet embed content from remote source.')
