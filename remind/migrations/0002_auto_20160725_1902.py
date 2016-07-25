# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remind', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remindme',
            name='date',
        ),
        migrations.RemoveField(
            model_name='remindme',
            name='time',
        ),
        migrations.AddField(
            model_name='remindme',
            name='date_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='remindme',
            name='email',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='remindme',
            name='message',
            field=models.CharField(null=True, max_length=1000, blank=True),
        ),
    ]
