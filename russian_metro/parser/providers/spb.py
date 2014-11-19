# -*- coding: utf-8 -*-
import re
from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    metro_data_src = u"http://ru.wikipedia.org/wiki/\
                       Линии_и_станции_Петербургского_метрополитена"
    header_marker = u'линия'
    title_re = re.compile(ur'.*?(\d{1,2}).*?\((.*?)\)', re.U | re.S)

    def download_all(self):
        html = BeautifulSoup(requests.get(self.metro_data_src).content)
        headers = html.find_all(class_='mw-headline')
        lines = self.line_model.get_all()
        for row in headers:
            header = row.find('font')
            if header and header.string.lower().find(self.header_marker) > -1:
                matches = title_re.match(header.string)
                if matches:
                    # extract all line data
                    line_color = header['color']
                    line_number = matches.group(1)
                    line_title = matches.group(2)
                    if not line_number in lines:
                        self.line_model.objects.create(
                            number=line_number,
                            color=line_color,
                            title=line_title
                        )
                    # extract stations
                    stations_ul = header.parent.find_next_sibling('ul')
                    for item in stations_ul.find_all('li'):
                        print item.string
