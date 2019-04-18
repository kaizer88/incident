# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-01 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0039_auto_20180529_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledriver',
            name='reason',
            field=models.CharField(choices=[(b'discretionary change', b'Discretionary Vehicle Change'), (b'new employee', b'New Employee'), (b'pool car', b'Pool Car'), (b'relocation', b'Relocation'), (b'temp vehicle', b'Temp Vehicle')], max_length=255),
        ),
    ]
