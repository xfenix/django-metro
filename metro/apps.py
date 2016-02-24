# -*- coding: utf-8 -*-
from django.conf import settings
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MetroConfig(AppConfig):
    name = 'metro'
    verbose_name = getattr(settings, 'METRO_APP_TITLE', _('Metro'))
