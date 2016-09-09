# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Станция метро',
                'ordering': ['order'],
                'verbose_name_plural': 'Станции метро',
            },
        ),
        migrations.CreateModel(
            name='MetroLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Номер линии')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='metro/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Линия метро',
                'ordering': ['number'],
                'verbose_name_plural': 'Линии метро',
            },
        ),
        migrations.AddField(
            model_name='metro',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metro.MetroLine', verbose_name='Линия метро'),
        ),
    ]
