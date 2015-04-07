# -*- coding: utf-8 -*-
from sc.adshelper.config import PROJECTNAME
from plone.app.upgrade.utils import loadMigrationProfile

import logging


def apply_profile(context):
    """Atualiza perfil para versao 2."""
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-sc.adshelper.upgrades.v2:default'
    loadMigrationProfile(context, profile)
    logger.info('Atualizado para versao 2')
