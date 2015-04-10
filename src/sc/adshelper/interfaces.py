# -*- coding: utf-8 -*-
from plone.directives import form
from sc.adshelper import _
from zope import schema
from zope.interface import Interface


class IBrowserLayer(Interface):

    """A layer specific for this add-on product."""


class IAdsHelperSettings(form.Schema):

    """Schema for the control panel form."""

    show_authenticated = schema.Bool(
        title=_(u'Show to authenticated users?'),
        description=_(
            u'By default, viewlets will be visible for anonymous users only.'
            u'If selected, the code will be shown to authenticated users also.'
        ),
        default=False,
    )

    html_head = schema.Text(
        title=_(u'HTML Head'),
        description=_(u'This code will be included inside the head tag.'),
        default=u'',
        required=False,
    )

    above_content = schema.Text(
        title=_(u'Above Content'),
        description=_(u'This code will be included above the content of the page.'),
        default=u'',
        required=False,
    )

    below_content = schema.Text(
        title=_(u'Below Content'),
        description=_(u'This code will be included above the content of the page.'),
        default=u'',
        required=False,
    )

    footer = schema.Text(
        title=_(u'Footer'),
        description=_(u'This code will be included at the end of the page.'),
        default=u'',
        required=False,
    )
