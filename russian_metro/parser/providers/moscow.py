# -*- coding: utf-8 -*-
from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    metro_lines_src = u"http://ru.wikipedia.org/wiki/Модуль:MoscowMetro#ColorByNum"
    metro_stations_src = u"http://ru.wikipedia.org/w/index.php?title=\
                           Список_станций_Московского_метрополитена"

    def download_lines(self):
        html = BeautifulSoup(requests.get(self.metro_lines_src).content)
        table = html.find('table')
        lines = dict()
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
                self.line_model.objects.get_or_create(
                    number=number,
                    defaults=dict(
                        title=title, color='#' + color
                    )
                )

    def download_stations(self):
        html = BeautifulSoup(requests.get(self.metro_stations_src).content)
        table = html.find('table', 'wikitable')
        lines = self.line_model.get_all()
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
                    title = cell.find('span').string
            try:
                line_inst = lines[line]
            except KeyError:
                logger.warning(
                    u'MetroLine with number %d does not exist' % line
                )
                continue
            self.station_model\
                .objects\
                .get_or_create(line=line_inst, title=title)
