# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

from metro.parser.base import BaseRuDataProvider


class DataProvider(BaseRuDataProvider):
    metro_data_src = "http://ru.wikipedia.org/w/index.php?title=\
                       Список_станций_Минского_метрополитена"

    def download_all(self):
        self.parse_usual_big_table(station_td_count=5)
