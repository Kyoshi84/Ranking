# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-15 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0041_tournamentstandings_player_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('fblink', models.CharField(default='https://www.facebook.com/Unclekyoshi/posts/2080173272212700', max_length=500, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Wiadomo\u015bci',
            },
        ),
    ]