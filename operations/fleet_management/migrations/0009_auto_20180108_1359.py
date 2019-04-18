# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 11:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0008_auto_20180105_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvehicletyre',
            name='make',
            field=models.CharField(max_length=255, verbose_name=b'Make'),
        ),
        migrations.AlterField(
            model_name='historicalvehicletyre',
            name='mileage_at_replacement',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Mileage At Replacement'),
        ),
        migrations.AlterField(
            model_name='historicalvehicletyre',
            name='position',
            field=models.CharField(choices=[(b'fr', b'Front Right'), (b'fl', b'Front Left'), (b'rr', b'Rear Right'), (b'rl', b'Rear Left'), (b'spare', b'Spare')], max_length=50, verbose_name=b'Position'),
        ),
        migrations.AlterField(
            model_name='historicalvehicletyre',
            name='serial_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Serial Number'),
        ),
        migrations.AlterField(
            model_name='historicalvehicletyre',
            name='size',
            field=models.CharField(max_length=255, verbose_name=b'Size'),
        ),
        migrations.AlterField(
            model_name='vehicletyre',
            name='make',
            field=models.CharField(max_length=255, verbose_name=b'Make'),
        ),
        migrations.AlterField(
            model_name='vehicletyre',
            name='mileage_at_replacement',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Mileage At Replacement'),
        ),
        migrations.AlterField(
            model_name='vehicletyre',
            name='position',
            field=models.CharField(choices=[(b'fr', b'Front Right'), (b'fl', b'Front Left'), (b'rr', b'Rear Right'), (b'rl', b'Rear Left'), (b'spare', b'Spare')], max_length=50, verbose_name=b'Position'),
        ),
        migrations.AlterField(
            model_name='vehicletyre',
            name='serial_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Serial Number'),
        ),
        migrations.AlterField(
            model_name='vehicletyre',
            name='size',
            field=models.CharField(max_length=255, verbose_name=b'Size'),
        ),
    ]
