# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    metro_data_src = u"http://ru.wikipedia.org/wiki/\
                       Список_станций_Екатеринбургского_метрополитена"

    def download_all(self):
        self.parse_usual_big_table(table_number=2)
