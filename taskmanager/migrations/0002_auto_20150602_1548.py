# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_added',
            field=models.DateTimeField(default=None, null=True, verbose_name=b'date added', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'last modified', blank=True),
        ),
    ]
