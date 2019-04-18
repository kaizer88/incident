# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-10 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0076_auto_20180803_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelCardUsageTransactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('changed_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'default_permissions': [],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='fuelcardusage',
            name='date_used',
            field=models.DateTimeField(verbose_name=b'Transaction Date'),
        ),
        migrations.RemoveField(
            model_name='fuelcardusage',
            name='transaction_type',
        ),
        migrations.AddField(
            model_name='fuelcardusage',
            name='transaction_type',
            field=models.ManyToManyField(to='fleet_management.FuelCardUsageTransactionType', verbose_name=b'Transaction Type'),
        ),
    ]
