# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-28 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OverallStandings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Imi\u0119')),
                ('nicname', models.CharField(blank=True, max_length=50, verbose_name='Pseudonim')),
                ('army', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('player_num', models.IntegerField()),
                ('points', models.IntegerField()),
                ('ranting', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TournamentStandings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_place', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Player')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Tournament')),
            ],
        ),
        migrations.AddField(
            model_name='overallstandings',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Player'),
        ),
    ]
