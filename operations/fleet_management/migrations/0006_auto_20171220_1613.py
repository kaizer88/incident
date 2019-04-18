# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0005_merge_20171213_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelcard',
            name='card_type',
            field=models.CharField(choices=[(b'fuel', b'Fuel Only'), (b'fuel oil', b'Fuel & Oil'), (b'fuel oil toll', b'Fuel, Oil & Toll'), (b'fuel oil etag', b'Fuel, Oil & eTag')], max_length=255),
        ),
        migrations.AlterField(
            model_name='historicalfuelcard',
            name='card_type',
            field=models.CharField(choices=[(b'fuel', b'Fuel Only'), (b'fuel oil', b'Fuel & Oil'), (b'fuel oil toll', b'Fuel, Oil & Toll'), (b'fuel oil etag', b'Fuel, Oil & eTag')], max_length=255),
        ),
    ]