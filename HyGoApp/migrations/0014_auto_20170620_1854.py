# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HyGoApp', '0013_auto_20170620_1853'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clicks',
            new_name='Click',
        ),
    ]
