# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HyGoApp', '0012_click'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Click',
            new_name='Clicks',
        ),
    ]
