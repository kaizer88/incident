# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-18 09:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0064_merge_20180711_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpurchasedetail',
            name='purchase_type',
            field=models.CharField(choices=[(b'cash', b'Cash'), (b'hp', b'HP - Hire Purchase'), (b'lease', b'Lease')], max_length=50, verbose_name=b'Purchase Type'),
        ),
        migrations.AlterField(
            model_name='historicalvehicle',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date Accepted'),
        ),
        migrations.AlterField(
            model_name='historicalvehicle',
            name='delivery_location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Accepted Location'),
        ),
        migrations.AlterField(
            model_name='historicalvehicle',
            name='delivery_odometer_mileage',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Accepted Odometer Mileage'),
        ),
        migrations.AlterField(
            model_name='historicalvehicle',
            name='rental_contact_person',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Rental Company Contact Person'),
        ),
        migrations.AlterField(
            model_name='historicalvehicle',
            name='returned_location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Return Location'),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='claim_type',
            field=models.CharField(choices=[(b'', b'--- Select Answer ---'), (b'accident claim', b'Accident Claim'), (b'vehicle theft', b'Vehicle Theft'), (b'other', b'Other')], max_length=50, verbose_name=b'Claim Type'),
        ),
        migrations.AlterField(
            model_name='purchasedetail',
            name='purchase_type',
            field=models.CharField(choices=[(b'cash', b'Cash'), (b'hp', b'HP - Hire Purchase'), (b'lease', b'Lease')], max_length=50, verbose_name=b'Purchase Type'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date Accepted'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='delivery_location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Accepted Location'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='delivery_odometer_mileage',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Accepted Odometer Mileage'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='rental_contact_person',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Rental Company Contact Person'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='returned_location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Return Location'),
        ),
    ]
