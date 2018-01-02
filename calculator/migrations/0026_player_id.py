# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0025_auto_20171125_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True),
        ),
    ]
