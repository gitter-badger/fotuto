# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0002_auto_20150224_1114'),
        ('vars', '0004_auto_20150215_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mimic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('x', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('y', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('vars', models.ManyToManyField(to='vars.Var', null=True, blank=True)),
                ('window', models.ForeignKey(to='windows.Window')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
