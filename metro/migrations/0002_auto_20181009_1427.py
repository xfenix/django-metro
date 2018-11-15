# Generated by Django 2.1.2 on 2018-10-09 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metro',
            options={'ordering': ['order'], 'verbose_name': 'Metro station', 'verbose_name_plural': 'Metro stations'},
        ),
        migrations.AlterModelOptions(
            name='metroline',
            options={'ordering': ['number'], 'verbose_name': 'Metro line', 'verbose_name_plural': 'Metro lines'},
        ),
        migrations.AlterField(
            model_name='metro',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metro.MetroLine', verbose_name='Metro line'),
        ),
        migrations.AlterField(
            model_name='metro',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='metro',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='metroline',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='metroline',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='metro/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='metroline',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Line number'),
        ),
        migrations.AlterField(
            model_name='metroline',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]