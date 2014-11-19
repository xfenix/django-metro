# -*- coding: utf-8 -*-
import logging
import requests
from django.db import models
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


class MetroLine(models.Model):
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

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = u'Станция метро'
        verbose_name_plural = u'Станции метро'
