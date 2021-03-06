# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_description', models.CharField(max_length=200)),
                ('long_description', models.TextField()),
                ('deadline', models.DateField()),
                ('date_added', models.DateTimeField(verbose_name=b'date added')),
                ('last_modified', models.DateTimeField(verbose_name=b'last modified')),
            ],
        ),
    ]
