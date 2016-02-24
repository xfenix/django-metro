# -*- coding: utf-8 -*-
from metro.parser.base import BaseRuDataProvider


class DataProvider(BaseRuDataProvider):
    def download_all(self):
        # yeap, Omsk
        self.get_or_create_station(
            self.get_or_create_line(
                1, 'Первая', 'red'
            ),
            'Библиотека имени Пушкина'
        )
