# -*- coding: utf-8 -*-
import requests
from django.db import models
from django.utils.translation import ugettext as _


class MetroLine(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_(u'Название')
    )
    color = models.CharField(
        max_length=255,
        verbose_name=_(u'Цвет'),
        blank=True,
        null=True,
    )
    number = models.IntegerField(
        verbose_name=_(u'Номер линии'),
        help_text=_(u'Реальный номер линии'),
        null=True,
        blank=True
    )
    icon = models.ImageField(
        upload_to='metro/',
        verbose_name=_(u'Иконка'),
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
    get_admin_color.short_description = _(u'Цвет')

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['number']
        verbose_name = _(u'Линия метро')
        verbose_name_plural = _(u'Линии метро')


class Metro(models.Model):
    line = models.ForeignKey(
        MetroLine,
        verbose_name=_(u'Линия метро')
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_(u'Название')
    )
    order = models.PositiveIntegerField(
        verbose_name=_(u'Сортировка'),
        default=0,
    )

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = _(u'Станция метро')
        verbose_name_plural = _(u'Станции метро')
