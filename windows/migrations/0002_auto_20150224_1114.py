# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='window',
            name='title',
            field=models.CharField(default=b'Untitled', max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
