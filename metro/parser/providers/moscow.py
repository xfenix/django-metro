# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from metro.parser.base import BaseRuDataProvider


class DataProvider(BaseRuDataProvider):
    metro_lines_src = "http://ru.wikipedia.org/wiki/Модуль:MoscowMetro#ColorByNum"
    metro_stations_src = "http://ru.wikipedia.org/w/index.php?title=\
                           Список_станций_Московского_метрополитена"

    def download_lines(self):
        html = self.create_dom(self.metro_lines_src)
        table = html.find('table', 'wikitable')
        for i, row in enumerate(table.find_all('tr')):
            if i == 0:
                continue
            number = 0
            for j, cell in enumerate(row.find_all('td')):
                value = cell.string
                if j == 0:
                    if value and value.isdigit():
                        number = int(value)
                elif j == 1:
                    title = value
                elif j == 2:
                    color = value
            if number > 0:
                self.get_or_create_line(number, title, '#' + color)

    def download_stations(self):
        html = self.create_dom(self.metro_stations_src)
        tables = html.find_all('table', 'standard')
        lines = self.line_model.get_all()
        for table in tables:
            for i, row in enumerate(table.find_all('tr')):
                if i == 0:
                    continue
                for j, cell in enumerate(row.find_all('td')):
                    if j == 0:
                        line = 0
                        value = cell.find('span', 'sortkey').string
                        if value and value.isdigit():
                            line = int(value)
                    elif j == 1:
                        title = cell.find('a').text.strip()
                try:
                    line_inst = lines[line]
                except KeyError:
                    continue
                self.get_or_create_station(line_inst, title)
