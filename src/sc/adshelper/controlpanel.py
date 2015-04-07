# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from sc.adshelper import _
from sc.adshelper.interfaces import IAdsHelperSettings


class AdsHelperSettingsEditForm(controlpanel.RegistryEditForm):

    """Control panel edit form."""

    schema = IAdsHelperSettings
    label = _(u'Ads Helper')
    description = _(u'Settings for the sc.adshelper package')


class AdsHelperSettingsControlPanel(controlpanel.ControlPanelFormWrapper):

    """Control panel form wrapper."""

    form = AdsHelperSettingsEditForm
