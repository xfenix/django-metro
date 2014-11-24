# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': '\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u043c\u0435\u0442\u0440\u043e',
                'verbose_name_plural': '\u0421\u0442\u0430\u043d\u0446\u0438\u0438 \u043c\u0435\u0442\u0440\u043e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MetroLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('color', models.CharField(max_length=255, null=True, verbose_name='\u0426\u0432\u0435\u0442', blank=True)),
                ('number', models.IntegerField(null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043b\u0438\u043d\u0438\u0438', blank=True)),
                ('icon', models.ImageField(upload_to=b'metro/', null=True, verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430', blank=True)),
            ],
            options={
                'ordering': ['number'],
                'verbose_name': '\u041b\u0438\u043d\u0438\u044f \u043c\u0435\u0442\u0440\u043e',
                'verbose_name_plural': '\u041b\u0438\u043d\u0438\u0438 \u043c\u0435\u0442\u0440\u043e',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='metro',
            name='line',
            field=models.ForeignKey(verbose_name='\u041b\u0438\u043d\u0438\u044f \u043c\u0435\u0442\u0440\u043e', to='metro.MetroLine'),
            preserve_default=True,
        ),
    ]
