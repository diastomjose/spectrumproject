# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-06 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placelist',
            name='place_description',
            field=models.CharField(default='hello', max_length=1500),
            preserve_default=False,
        ),
    ]
