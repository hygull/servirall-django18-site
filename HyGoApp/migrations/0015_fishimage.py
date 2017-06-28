# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import HyGoApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('HyGoApp', '0014_auto_20170620_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='FishImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flesh_name', models.CharField(max_length=50)),
                ('flesh_pic', models.ImageField(default=b'https://en.wikipedia.org/wiki/List_of_types_of_seafood#/media/File:Squilla_mantis_(l%27Ametlla)_brighter_and_quality.jpg', max_length=200, upload_to=b'')),
                ('flesh_type', models.IntegerField(default=b'Type0', blank=True, choices=[(1, b'Type1'), (2, b'Type2'), (3, b'Type3'), (4, b'Type4'), (5, b'Type5'), (6, b'Type6'), (7, b'Other')])),
                ('price', models.FloatField()),
                ('discount', models.IntegerField(default=0, blank=True, validators=[HyGoApp.models.validate_discount])),
            ],
        ),
    ]
