# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from metro.parser.base import BaseRuDataProvider


class DataProvider(BaseRuDataProvider):
    metro_data_src = "http://ru.wikipedia.org/wiki/\
                       Список_станций_Екатеринбургского_метрополитена"
    unknown = 'неизвестн'

    def download_all(self):
        html = self.create_dom(self.metro_data_src)
        # i dont want to parse this station, im tired
        line = self.get_or_create_line(1, 'Первая', 'green')
        # get stations
        table = html.find('table', class_='wide')
        for cell in table.find_all('tr'):
            tds = cell.find_all('td', recursive=False)
            if tds and len(tds) > 1:
                if tds[1].get_text().find(self.unknown) == -1:
                    self.get_or_create_station(line, tds[0])
