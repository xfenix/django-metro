# -*- coding: utf-8 -*-
from importlib import import_module
from django.conf import settings

from moscow_metro.models import Metro, MetroLine


providers_path = 'moscow_metro.parser.providers'
metro_city = None
provider = None

# hello, default city
if not hasattr(settings, 'RUMETRO_CITY'):
    metro_city = u'moscow'
else:
    metro_city = settings.RUMETRO_CITY

# import data provider
try:
    module = import_module(
        '%s.%s' % (providers_path, metro_city.lower())
    )
    provider = module.DataProvider(
        station_model=Metro, line_model=MetroLine
    )
except ImportError:
    raise NotImplementedError(
        u'Provider for this city does not implemented'
    )
