# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import HyGoApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('HyGoApp', '0015_fishimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='fishimage',
            name='description',
            field=models.TextField(default=b'Fish are vertebrates which live in water and respire (get oxygen) with gills. They lack limbs with digits (fingers & toes).\nThis is a definition which does not quite work: some amphibia also live in water and have external gills, but they are not fishes.', validators=[HyGoApp.models.validate_description]),
        ),
    ]
