# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0022_delete_overallstandings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='army',
        ),
        migrations.AddField(
            model_name='player',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='tournamentstandings',
            name='army',
            field=models.CharField(blank=True, max_length=20, verbose_name='Armia'),
        ),
    ]