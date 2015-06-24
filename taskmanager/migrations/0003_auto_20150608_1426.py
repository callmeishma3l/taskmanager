# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20150602_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date added', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'last modified', null=True),
        ),
    ]
