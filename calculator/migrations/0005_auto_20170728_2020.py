# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-28 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_auto_20170728_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=4, null=True),
        ),
    ]
