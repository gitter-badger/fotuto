# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vars', '0002_auto_20150210_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='var',
            name='value',
            field=models.FloatField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='var',
            name='var_type',
            field=models.CharField(default=b'binary', max_length=10, verbose_name=b'Type', blank=True, choices=[(b'binary', b'Binary'), (b'real', b'Real')]),
            preserve_default=True,
        ),
    ]
