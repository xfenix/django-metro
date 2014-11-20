# -*- coding: utf-8 -*-
from django.conf import settings
from django.apps import AppConfig


class MetroConfig(AppConfig):
    name = u'russian_metro'
    verbose_name = getattr(settings, 'RUMETRO_APP_TITLE', u'Метро')
