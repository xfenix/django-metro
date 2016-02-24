# -*- coding: utf-8 -*-
from importlib import import_module
from django.conf import settings

from metro.models import Metro, MetroLine

provider = None

# import data provider
try:
    module = import_module(
        'metro.parser.providers.%s' % (
            getattr(settings, 'METRO_PROVIDER', 'moscow').lower()
        )
    )
    provider = module.DataProvider(
        station_model=Metro, line_model=MetroLine
    )
except ImportError:
    raise NotImplementedError(
        'Provider for this city does not implemented'
    )
