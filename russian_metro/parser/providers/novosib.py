# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    metro_data_src = u"http://ru.wikipedia.org/wiki/\
                       Список_станций_Новосибирского_метрополитена"

    def download_all(self):
        i = 0
        line_trs = []
        line_data = dict()
        html = self.create_dom(self.metro_data_src)
        table = html.find('table')
        stations = []
        for tr in table.find_all('tr', recursive=False):
            td = tr.find('td', recursive=False)
            if td:
                if self.line_word in td.get_text():
                    i += 1
                    line = self.get_or_create_line(i, td)
                elif line:
                    if 'colspan' in td.attrs:
                        break
                    self.get_or_create_station(line, td)
