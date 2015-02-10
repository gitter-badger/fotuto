# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True, max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('model', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True, max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('var_type', models.CharField(max_length=10, verbose_name=b'Type', choices=[(b'binary', b'Binary'), (b'real', b'Real')])),
                ('units', models.CharField(max_length=10, blank=True)),
                ('value', models.FloatField(default=0)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('device', models.ForeignKey(related_name='vars', to='vars.Device')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
