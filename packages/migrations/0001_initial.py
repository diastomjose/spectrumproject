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
            name='OptionalPlaceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=100)),
                ('place_name', models.CharField(max_length=100)),
                ('place_no', models.IntegerField()),
                ('place_cost', models.IntegerField()),
                ('place_pic', models.FileField(upload_to='media/product_pics')),
            ],
            options={
                'verbose_name': 'optional_place_name',
                'verbose_name_plural': 'optional_place_name',
            },
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=100)),
                ('package_no', models.IntegerField()),
                ('package_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('place_no', models.IntegerField()),
                ('package_name', models.CharField(max_length=100)),
                ('place_pic', models.FileField(upload_to='media/product_pics')),
            ],
            options={
                'verbose_name': 'place_name',
                'verbose_name_plural': 'place_name',
            },
        ),
        migrations.CreateModel(
            name='UserPackageList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('package_name', models.CharField(max_length=100)),
                ('totalcost', models.IntegerField()),
                ('allplaces', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'username',
                'verbose_name_plural': 'username',
            },
        ),
    ]
