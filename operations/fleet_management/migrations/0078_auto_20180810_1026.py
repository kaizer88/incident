# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-10 08:26
from __future__ import unicode_literals

from django.db import migrations
from fleet_management.models import FuelCardUsageTransactionType
def populate_transaction_types(apps, schema_editor):
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="CARD FEE")
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="COURIER SERVICE")
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="DAMAGED CRD_FEE")
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="EFT")
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="FUEL")
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="MAINTENANCE")
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="OIL")
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="TOLL-GATE")
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="TRANSACTION FEE")
	upload = FuelCardUsageTransactionType.objects.get_or_create(description="VAT OF SER FEES")


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0077_auto_20180810_1023'),
    ]

    operations = [
    	migrations.RunPython(populate_transaction_types)
    ]
