# -*- coding: utf-8 -*-
from importlib import import_module
from django.conf import settings

from russian_metro.models import Metro, MetroLine

provider = None

# import data provider
try:
    module = import_module(
        'russian_metro.parser.providers.%s' % (
            getattr(settings, 'RUMETRO_PROVIDER', u'moscow').lower()
        )
    )
    provider = module.DataProvider(
        station_model=Metro, line_model=MetroLine
    )
except ImportError:
    raise NotImplementedError(
        u'Provider for this city does not implemented'
    )
