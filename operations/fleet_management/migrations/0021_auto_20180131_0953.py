# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0020_auto_20180131_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelcard',
            name='card_type',
            field=models.CharField(choices=[(b'fuel only', b'Fuel Only'), (b'fuel & oil', b'Fuel & Oil'), (b'fuel, oil & toll', b'Fuel, Oil & Toll'), (b'fuel, oil & etag', b'Fuel, Oil & eTag')], max_length=255, verbose_name=b'Card Type'),
        ),
        migrations.AlterField(
            model_name='historicalfuelcard',
            name='card_type',
            field=models.CharField(choices=[(b'fuel only', b'Fuel Only'), (b'fuel & oil', b'Fuel & Oil'), (b'fuel, oil & toll', b'Fuel, Oil & Toll'), (b'fuel, oil & etag', b'Fuel, Oil & eTag')], max_length=255, verbose_name=b'Card Type'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='installation_type',
            field=models.CharField(choices=[(b'new', b'New'), (b'reinstall', b'Re-Install')], max_length=255, verbose_name=b'Installation Type'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='previous_vehicle_reg_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Previous Registration Number'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='purchase_type',
            field=models.CharField(choices=[(b'cash', b'Cash'), (b'rental', b'Rental')], max_length=255, verbose_name=b'Purchase Type'),
        ),
        migrations.AlterField(
            model_name='vehicledriver',
            name='start_date',
            field=models.DateTimeField(verbose_name=b'Start Date'),
        ),
    ]