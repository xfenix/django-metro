# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from metro.parser.base import BaseRuDataProvider


class DataProvider(BaseRuDataProvider):
    metro_data_src = "http://ru.wikipedia.org/wiki/\
                       Список_станций_Нижегородского_метрополитена"
    td_count = 4

    def download_all(self):
        i = 0
        line_trs = []
        line_data = dict()
        html = BeautifulSoup(requests.get(self.metro_data_src).content)
        headers = html.find_all('h2')
        for head in headers:
            if self.line_word in head.get_text():
                i += 1
                table = head.findNext('table')
                td = table.find('td')
                line = self.get_or_create_line(i, td)
                all_trs = table.find_all('tr', recursive=False)
                for tr in all_trs:
                    tds = tr.find_all('td', recursive=False)
                    if len(tds) == self.td_count:
                        self.get_or_create_station(line, tds[0])
