# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-28 10:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='ranting',
        ),
    ]
