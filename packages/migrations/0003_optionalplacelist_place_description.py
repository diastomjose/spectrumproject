# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-06 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_placelist_place_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionalplacelist',
            name='place_description',
            field=models.CharField(default='j', max_length=1500),
            preserve_default=False,
        ),
    ]