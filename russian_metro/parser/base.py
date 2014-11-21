# -*- coding: utf-8 -*-
import re
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
    clean_title_re = re.compile(ur'\s*\(.*\)')

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

    def get_or_create_line(self, i, el_or_title, color=None):
        is_tag = isinstance(el_or_title, Tag)
        line, _ = self.line_model.objects.get_or_create(
            **dict(
                number=i,
                defaults=dict(
                    title=self.prep_title(el_or_title),
                    color=self.prep_color(el_or_title if is_tag else color),
                )
            )
        )
        return line

    def get_or_create_station(self, line, el):
        station, _ = self.station_model.objects.get_or_create(
            line=line,
            title=self.prep_title(self.get_el_text(el)),
        )
        return station

    def get_el_text(self, el):
        return el.get_text() if isinstance(el, Tag) else unicode(el)

    def prep_title(self, el):
        return self.clean_title_re.sub(
            '', self.get_el_text(el).replace(self.line_word, '').strip()
        )

    def prep_color(self, el):
        try:
            return ( el['style'] if isinstance(el, Tag) else el)\
                .replace(self.bg_word, '').strip()
        except KeyError:
            return ''

    # universal cases
    def parse_usual_big_table(self, station_td_count=None, table_number=None):
        i = 0
        line = None
        html = self.create_dom(self.metro_data_src)
        # search only in body
        body = html.find(id='mw-content-text')
        if table_number:
            table = body.find_all('table')[table_number]
        else:
            table = body.find('table')
        # get tbody instead of table, if exist
        tbody = table.find('tbody', recursive=False)
        if tbody:
            table = tbody
        stations = []
        for tr in table.find_all('tr', recursive=False):
            td = tr.find('td', recursive=False)
            if td:
                if 'rowspan' in td.attrs:
                    continue
                if self.line_word in td.get_text():
                    i += 1
                    line = self.get_or_create_line(i, td)
                elif line:
                    if 'colspan' in td.attrs:
                        break
                    # additional check for some cases
                    if station_td_count:
                        count = len(
                            tr.find_all('td', recursive=False)
                        )
                        if count != station_td_count:
                            continue
                    self.get_or_create_station(line, td)
