# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class BaseDataProvider(object):
    """ basic data provider
    """
    # base models
    line_model = None
    station_model = None
    # various parser stuff
    line_word = u'линия'
    bg_word = 'background:'

    # main methods
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

    # helper methods
    def create_dom(self, url):
        get = lambda: BeautifulSoup(requests.get(url).content)
        try:
            html = get()
        except:
            # one more try
            try:
                html = get()
            except:
                return None
        return html

    def get_or_create_line(self, i, el, color=None):
        is_tag = isinstance(el, Tag)
        line, _ = self.line_model.objects.get_or_create(
            **dict(
                number=i,
                defaults=dict(
                    title=self.prep_title(el) if is_tag else el,
                    color=self.prep_color(el) if is_tag else color,
                )
            )
        )
        return line

    def get_or_create_station(self, line, el):
        station, _ = self.station_model.objects.get_or_create(
            line=line,
            title=el.get_text() if isinstance(el, Tag) else el,
        )
        return station

    def prep_title(self, s):
        try:
            return unicode(s.get_text())\
                .replace(self.line_word, '')\
                .strip()
        except:
            return ''

    def prep_color(self, el):
        try:
            return el['style'].replace(self.bg_word, '').strip()
        except KeyError:
            return ''
