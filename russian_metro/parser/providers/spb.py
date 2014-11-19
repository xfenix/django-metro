# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    metro_data_src = u"http://ru.wikipedia.org/wiki/\
                       Линии_и_станции_Петербургского_метрополитена"
    header_marker = u'линия'
    skip_from = 6 # 6, 7, 8 lines is under construction
    title_re = re.compile(ur'.*?(\d{1,2}).*?\((.*?)\)', re.U | re.S)

    def download_all(self):
        html = BeautifulSoup(requests.get(self.metro_data_src).content)
        headers = html.find_all(class_='mw-headline')
        lines = self.line_model.get_all()
        for row in headers:
            header = row.find('font')
            if header and header.string.lower().find(self.header_marker) > -1:
                matches = self.title_re.match(header.string)
                if matches:
                    # extract all line data
                    line_color = header['color']
                    line_number = int(matches.group(1))
                    if line_number >= self.skip_from:
                        continue
                    line_title = matches.group(2)
                    if not line_number in lines:
                        line = self.line_model.objects.create(
                            number=line_number,
                            color=line_color,
                            title=line_title
                        )
                    else:
                        line = lines[line_number]
                    # extract stations
                    stations_ul = header.parent.parent.find_next_sibling('ul')
                    if stations_ul:
                        for item in stations_ul.find_all('li'):
                            self.station_model.objects\
                                .get_or_create(
                                    title=item.string,
                                    line=line
                                )
