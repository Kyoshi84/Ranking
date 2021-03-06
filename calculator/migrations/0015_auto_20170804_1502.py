# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-04 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0014_auto_20170804_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='base_rating',
        ),
        migrations.AlterField(
            model_name='overallstandings',
            name='player_points',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='points',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tournamentstandings',
            name='player_place',
            field=models.FloatField(),
        ),
    ]
