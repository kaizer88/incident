# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 14:24
from __future__ import unicode_literals

from django.db import migrations

class Migration(migrations.Migration):

    def create_new_user_groups(apps, schema_editor):
        from django.core.management import call_command
        call_command('create_ops_groups')

    dependencies = [
        ('operations', '0008_auto_20180130_1257'),
    ]

    operations = [
        migrations.RunPython(create_new_user_groups),
    ]