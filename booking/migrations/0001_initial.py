# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_user', models.CharField(max_length=100)),
                ('booked_package', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'booked_user',
                'verbose_name_plural': 'booked_user',
            },
        ),
        migrations.CreateModel(
            name='PackagePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_price', models.IntegerField()),
                ('package_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'package_price',
                'verbose_name_plural': 'package_price',
            },
        ),
    ]
