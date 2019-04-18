# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 13:47
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import lib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0021_auto_20180131_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='vehicle',
            field=lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='incident_vehicle', to='fleet_management.Vehicle'),
        ),
    ]
