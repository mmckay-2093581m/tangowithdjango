# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20150120_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='viewsXX',
            new_name='views',
        ),
    ]
