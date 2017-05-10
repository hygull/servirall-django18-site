# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HyGoApp', '0009_markdown'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoVirtualReality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=150)),
            ],
        ),
    ]
