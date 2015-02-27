# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mimics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mimic',
            name='window',
            field=models.ForeignKey(related_name='mimics', to='windows.Window'),
            preserve_default=True,
        ),
    ]
