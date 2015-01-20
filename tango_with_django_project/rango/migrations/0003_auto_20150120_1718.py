# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150119_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=2),
        ),
    ]
