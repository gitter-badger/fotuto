# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vars', '0004_auto_20150215_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ('active', 'pk')},
        ),
        migrations.AlterModelOptions(
            name='var',
            options={'ordering': ('-active', 'device')},
        ),
        migrations.AlterField(
            model_name='var',
            name='var_type',
            field=models.CharField(default=b'binary', max_length=10, verbose_name=b'Type', blank=True, choices=[(b'binary', b'Digital'), (b'real', b'Analogic')]),
            preserve_default=True,
        ),
    ]
