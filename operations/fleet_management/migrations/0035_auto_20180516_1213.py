# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-16 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0034_auto_20180515_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financedetail',
            name='financier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfinancedetail',
            name='financier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]