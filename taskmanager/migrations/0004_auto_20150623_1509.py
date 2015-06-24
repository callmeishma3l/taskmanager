# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150623_1509'),
        ('taskmanager', '0003_auto_20150608_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('create_task', 'Can create new tasks'), ('edit_task', 'Can modify tasks'), ('remove    _task', 'Can delete tasks'))},
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_user',
            field=models.ForeignKey(default=None, to='account.MyUser', null=True),
        ),
    ]
