# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0017_auto_20170829_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retriever',
            name='indexer',
        ),
        migrations.AddField(
            model_name='retriever',
            name='algorithm',
            field=models.CharField(choices=[('L', 'LOPQ'), ('E', 'Exact')], db_index=True, default='E', max_length=1),
        ),
        migrations.AlterField(
            model_name='clustercodes',
            name='clusters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Retriever'),
        ),
        migrations.DeleteModel(
            name='Clusters',
        ),
    ]
