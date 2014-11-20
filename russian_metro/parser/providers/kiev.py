# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    metro_data_src = u"http://ru.wikipedia.org/wiki/\
                       Список_станций_Киевского_метрополитена"
    title_re = re.compile(ur'(.*?)\s+\(.*?\)', re.U | re.S)
    title_td_count = 7

    def download_all(self):
        i = 0
        line_trs = []
        line_data = dict()
        html = BeautifulSoup(requests.get(self.metro_data_src).content)
        tables = html.find_all('table')
        all_trs = tables[1].find_all('tr')
        # get list of lines
        for row in all_trs:
            td = row.find('td')
            if td:
                if 'colspan' in td.attrs and\
                   int(td['colspan']) == self.title_td_count:
                    i += 1
                    title_match = self.title_re.match(td.get_text())
                    line_color = td['style'].replace(u'background:', '')
                    line_trs.append(row)
                    line_data[row] = dict(
                        number=i,
                        defaults=dict(
                            title=title_match\
                                    .group(1)\
                                    .replace(u'линия', '')\
                                    .strip(),
                            color=line_color,
                        )
                    )
        # and now parse stations and create lines
        for row in all_trs:
            if row in line_trs:
                line, _ = self\
                    .line_model\
                    .objects\
                    .get_or_create(**line_data[row])
                for item in row.find_next_siblings('tr'):
                    # from one line to another
                    if item in line_trs:
                        break
                    td = item.find('td')
                    if td:
                        title_match = self.title_re.match(
                            td.get_text()
                        )
                        self.station_model\
                            .objects\
                            .get_or_create(
                                title=title_match.group(1),
                                line=line
                            )
