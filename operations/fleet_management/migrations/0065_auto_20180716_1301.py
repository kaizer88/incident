# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-16 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0064_merge_20180711_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceclaim',
            name='claim_type',
            field=models.CharField(choices=[(b'accident claim', b'Accident Claim'), (b'windscreen', b'Windscreen'), (b'vehicle theft', b'Vehicle Theft'), (b'other', b'Other')], max_length=50, verbose_name=b'Claim Type'),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='insurance_reference_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Claim Reference Number'),
        ),
    ]
