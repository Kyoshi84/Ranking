# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-28 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_remove_tournament_ranting'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]