# -*- coding: utf-8 -*-
from django.conf import settings
from django.apps import AppConfig


class MoscowMetroConfig(AppConfig):
    name = u'russian_metro'
    verbose_name = getattr(settings, 'RUMETRO_APP_TITLE', u'Метро')
