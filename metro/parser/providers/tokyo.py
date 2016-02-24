# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from metro.parser.base import BaseEnDataProvider


class DataProvider(BaseEnDataProvider):
    metro_lines_src = "%s/wiki/Tokyo_subway" % BaseEnDataProvider.base_en_url
    lines_buf = []

    def download_lines(self):
        html = self.create_dom(self.metro_lines_src)
        table = html.find_all('table')[2]
        for row in table.find_all('tr'):
            tds = row.find_all('td', recursive=False)
            if tds and len(tds) == 5:
                self.lines_buf.append(dict(
                    url=tds[3].find('a').attrs['href'],
                    color=self.prep_color(tds[0]),
                    title=self.prep_title(tds[3]),
                    number=self.get_el_text(tds[2])\
                                .replace('Line ', '')\
                                .strip()
                ))

    def download_stations(self):
        # very slow (13 http queries, i preffer scrapy, but...)
        for line in self.lines_buf:
            # create line
            line_inst = self.get_or_create_line(
                line['number'], line['title'], line['color']
            )
            print('Download stations for line number %s' % line['number'])
            # download stations
            url = BaseEnDataProvider.base_en_url + line['url']
            html = self.create_dom(url)
            table = html.find('table', class_='wikitable')
            for row in table.find_all('tr', recursive=False):
                tds = row.find_all('td', recursive=False)
                th = row.find('th')
                if tds and len(tds) > 1:
                    index = 0 if th else 1
                    self.get_or_create_station(
                        line_inst, self.get_el_text(tds[index])
                    )
