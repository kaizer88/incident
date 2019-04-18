# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-25 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0067_auto_20180724_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='driver_co_payment',
            field=models.CharField(choices=[(b'yes', b'Yes'), (b'no', b'No')], default=django.utils.timezone.now, max_length=255, verbose_name=b'Driver Co Payment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='invoice_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'Invoice Amount'),
        ),
        migrations.AddField(
            model_name='incident',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Invoice Number'),
        ),
        migrations.AddField(
            model_name='incident',
            name='percentage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='share_amount',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Share Amount'),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='driver_co_payment',
            field=models.CharField(choices=[(b'yes', b'Yes'), (b'no', b'No')], default=django.utils.timezone.now, max_length=255, verbose_name=b'Driver Co Payment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='invoice_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'Invoice Amount'),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Invoice Number'),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='percentage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='share_amount',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Share Amount'),
        ),
    ]
