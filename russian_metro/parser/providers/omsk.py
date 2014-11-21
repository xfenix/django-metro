# -*- coding: utf-8 -*-
from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    def download_all(self):
        # yeap, Omsk
        self.get_or_create_station(
            self.get_or_create_line(
                1, u'Первая', 'red'
            ),
            u'Библиотека имени Пушкина'
        )
