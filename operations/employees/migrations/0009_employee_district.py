# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-02-14 07:17
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import lib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0023_auto_20180828_0917'),
        ('employees', '0008_employee_cell_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='district',
            field=lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employees_in_branch', to='operations.Branch'),
        ),
    ]