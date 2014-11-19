# -*- coding: utf-8 -*-


class BaseDataProvider(object):
    """ basic data provider
    """
    line_model = None
    station_model = None

    def __init__(self, station_model=None, line_model=None):
        if station_model and line_model:
            self.station_model = station_model
            self.line_model = line_model
        else:
            raise AttributeError(
                u'You need to provide base station and line models'
            )

    def download_all(self):
        self.download_lines()
        self.download_stations()

    def download_lines(self):
        pass

    def download_stations(self):
        pass
