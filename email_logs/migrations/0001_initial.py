# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('receiver', models.TextField()),
                ('subject', models.TextField()),
                ('email', models.TextField()),
                ('timestamp', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
