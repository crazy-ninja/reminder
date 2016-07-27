# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemindMe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
