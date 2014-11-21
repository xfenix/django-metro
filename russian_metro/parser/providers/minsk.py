# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    metro_data_src = u"http://ru.wikipedia.org/w/index.php?title=\
                       Список_станций_Минского_метрополитена"

    def download_all(self):
        self.parse_usual_big_table(station_td_count=5)
