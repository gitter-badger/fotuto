# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vars', '0003_auto_20150210_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='address',
            field=models.CharField(unique=True, max_length=16),
            preserve_default=True,
        ),
    ]
