# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0002_auto_20150224_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='window',
            name='title',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
