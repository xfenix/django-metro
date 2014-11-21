# -*- coding: utf-8 -*-
from russian_metro.parser.base import BaseDataProvider


class DataProvider(BaseDataProvider):
    def download_all(self):
        # yeap, Omsk
        line, _ = self.line_model.objects\
            .get_or_create(
                color='red',
                title=u'Первая',
                number=1
            )
        self.station_model.objects\
            .get_or_create(
                title=u'Библиотека имени Пушкина',
                line=line
            )
