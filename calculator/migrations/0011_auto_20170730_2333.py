# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-30 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0010_auto_20170730_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]
