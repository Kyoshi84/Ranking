# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0027_remove_player_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Imi\u0119'),
        ),
    ]
