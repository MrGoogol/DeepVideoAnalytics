# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-31 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0056_auto_20171230_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='tevent',
            name='task_group_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
