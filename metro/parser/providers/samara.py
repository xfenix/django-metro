# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from metro.parser.base import BaseRuDataProvider


class DataProvider(BaseRuDataProvider):
    metro_data_src = "http://ru.wikipedia.org/wiki/\
                       Список_станций_Самарского_метрополитена"

    def download_all(self):
        self.parse_usual_big_table()
