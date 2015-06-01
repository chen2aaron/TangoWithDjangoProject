# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150601_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='catagory',
            new_name='category',
        ),
    ]
