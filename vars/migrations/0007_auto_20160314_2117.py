# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vars', '0006_auto_20160314_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
