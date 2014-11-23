# -*- coding: utf-8 -*-
import requests
from django.db import models
from django.utils.translation import ugettext as _


class MetroLine(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_(u'Title')
    )
    color = models.CharField(
        max_length=255,
        verbose_name=_(u'Color'),
        blank=True,
        null=True,
    )
    number = models.IntegerField(
        verbose_name=_(u'Line number'),
        null=True,
        blank=True
    )
    icon = models.ImageField(
        upload_to='metro/',
        verbose_name=_(u'Icon'),
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
    get_admin_color.short_description = _(u'Color')

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['number']
        verbose_name = _(u'Metro line')
        verbose_name_plural = _(u'Metro lines')


class Metro(models.Model):
    line = models.ForeignKey(
        MetroLine,
        verbose_name=_(u'Metro line')
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_(u'Title')
    )
    order = models.PositiveIntegerField(
        verbose_name=_(u'Order'),
        default=0,
    )

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = _(u'Metro station')
        verbose_name_plural = _(u'Metro stations')
