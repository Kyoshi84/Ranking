# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0030_timeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentstandings',
            name='player_points',
            field=models.FloatField(blank=True, default=1, verbose_name='Punkty Rankingu'),
            preserve_default=False,
        ),
    ]
