# -*- coding: utf-8 -*-
from plone.directives import form
from sc.adshelper import _
from zope import schema
from zope.interface import Interface


class IBrowserLayer(Interface):

    """A layer specific for this add-on product."""


class IAdsHelperSettings(form.Schema):

    """Schema for the control panel form."""

    head = schema.Text(
        title=_(u'Head'),
        description=_(u'This code will be included inside the head tag.'),
        required=False,
    )
