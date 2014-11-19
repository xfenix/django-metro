# -*- coding: utf-8 -*-
import logging
import requests
from django.db import models
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


class MetroLine(models.Model):
    SOURCE = u"http://ru.wikipedia.org/wiki/Модуль:MoscowMetro#ColorByNum"
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    color = models.CharField(
        max_length=255,
        verbose_name=u'Цвет',
        blank=True,
        null=True,
    )
    number = models.IntegerField(
        verbose_name=u'Номер линии',
        help_text=u'Реальный номер линии',
        null=True,
        blank=True
    )
    icon = models.ImageField(
        upload_to='metro/',
        verbose_name=u'Иконка',
        blank=True,
        null=True,
    )

    @classmethod
    def parse(cls):
        html = BeautifulSoup(requests.get(cls.SOURCE).content)
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
                try:
                    MetroLine.objects.get(number=number)
                except MetroLine.DoesNotExist:
                    MetroLine.objects.create(
                        number=number, title=title, color='#' + color
                    )

    @classmethod
    def get_all(cls):
        items = cls.objects.all()
        result = dict()
        for item in items:
            result[ item.number ] = item
        return result

    def get_admin_color(self):
        return u'<div style="width: 60px; height: 20px; '\
                'background: %s"></div>' % self.color
    get_admin_color.allow_tags = True
    get_admin_color.short_description = u'Цвет'

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['number']
        verbose_name = u'Линия метро'
        verbose_name_plural = u'Линии метро'


class Metro(models.Model):
    SOURCE = u"http://ru.wikipedia.org/w/index.php?title=\
               Список_станций_Московского_метрополитена"
    SKIP_STEPS = 2
    line = models.ForeignKey(
        MetroLine,
        verbose_name=u'Линия метро'
    )
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )
    order = models.PositiveIntegerField(
        verbose_name=u'Сортировка',
        default=0,
    )

    @classmethod
    def parse(cls):
        html = BeautifulSoup(requests.get(cls.SOURCE).content)
        table = html.find('table', 'wikitable')
        lines = MetroLine.get_all()
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
            Metro.objects.get_or_create(line=line_inst, title=title)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = u'Станция метро'
        verbose_name_plural = u'Станции метро'


def load():
    MetroLine.parse()
    Metro.parse()
