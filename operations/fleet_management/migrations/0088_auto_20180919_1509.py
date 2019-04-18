# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-19 13:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0087_merge_20180911_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicebooking',
            name='document_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name=b'cost'),
        ),
    ]