# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    metro_data_src = u"http://ru.wikipedia.org/w/index.php?title=\
                       Список_станций_Минского_метрополитена"
    title_re = re.compile(ur'(.*?)\s+\(.*?\)', re.U | re.S)
    title_td_count = 5

    def download_all(self):
        html = BeautifulSoup(requests.get(self.metro_data_src).content)
        table = html.find('table')
        line_trs = []
        line_data = dict()
        all_trs = table.find_all('tr')
        i = 0
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
                    if len(item.find_all('td')) == self.title_td_count:
                        self.get_or_create_station(line, item.find('td'))
