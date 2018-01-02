# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-31 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0020_auto_20170805_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overallstandings',
            name='player',
        ),
        migrations.DeleteModel(
            name='OverallStandings',
        ),
        migrations.CreateModel(
            name='OverallStandings',
            fields=[
            ],
            options={
                'verbose_name': 'Ranking',
                'proxy': True,
                'verbose_name_plural': 'Rankingi',
            },
            bases=('calculator.tournamentstandings',),
        ),
    ]
