# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from metro.parser.base import BaseEnDataProvider


class DataProvider(BaseEnDataProvider):
    metro_lines_src = "%s/wiki/London_Underground" % BaseEnDataProvider.base_en_url
    lines_buf = []

    def download_lines(self):
        html = self.create_dom(self.metro_lines_src)
        table = html.find('table', class_='wikitable')
        i = 0
        for row in table.find_all('tr', recursive=False):
            tds = row.find_all('td', recursive=False)
            if tds and len(tds) > 1:
                i += 1
                self.lines_buf.append(dict(
                    url=tds[0].find('a').attrs['href'],
                    # very bad
                    color=self.prep_color(tds[1])\
                        .replace('color:', '')\
                        .replace('white', '')\
                        .replace('black', '')\
                        .strip(),
                    title=self.prep_title(tds[0]),
                    number=i
                ))

    def download_stations(self):
        for line in self.lines_buf:
            # create line
            line_inst = self.get_or_create_line(
                line['number'], line['title'], line['color']
            )
            print('Download stations for line number %s' % line['number'])
            # download stations
            url = BaseEnDataProvider.base_en_url + line['url']
            html = self.create_dom(url)
            tables = html.find_all('table', class_='wikitable')
            for table in tables:
                for row in table.find_all('tr', recursive=False):
                    tds = row.find_all('td', recursive=False)
                    if tds and len(tds) > 1:
                        self.get_or_create_station(
                            line_inst, self.get_el_text(tds[0])
                        )
