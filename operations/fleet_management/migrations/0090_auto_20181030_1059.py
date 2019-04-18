# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-30 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0089_merge_20180926_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelcard',
            name='date_ordered',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date Ordered'),
        ),
        migrations.AddField(
            model_name='fuelcard',
            name='delivery_destination',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Delivery Destination'),
        ),
        migrations.AddField(
            model_name='fuelcard',
            name='new_card_ordered',
            field=models.CharField(blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')], max_length=255, null=True, verbose_name=b'New Card Ordered'),
        ),
        migrations.AddField(
            model_name='historicalfuelcard',
            name='date_ordered',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date Ordered'),
        ),
        migrations.AddField(
            model_name='historicalfuelcard',
            name='delivery_destination',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Delivery Destination'),
        ),
        migrations.AddField(
            model_name='historicalfuelcard',
            name='new_card_ordered',
            field=models.CharField(blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')], max_length=255, null=True, verbose_name=b'New Card Ordered'),
        ),
    ]
