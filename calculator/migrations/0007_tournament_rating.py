# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-28 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_remove_tournament_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=4),
            preserve_default=False,
        ),
    ]
