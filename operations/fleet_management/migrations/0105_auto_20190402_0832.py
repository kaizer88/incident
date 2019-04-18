# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-04-02 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0104_merge_20190313_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='insuranceclaim',
            name='boot_door',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='capets',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='car_top',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='ceiling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='chasis',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='dashboard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='dashboard_controls',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='door_panels',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='engine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='foot_pedals',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='front_bumper',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='gear_box',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='grill',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='hand_brake',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='hood',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_front_door',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_front_door_window',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_front_fender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_front_seat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_front_wheel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_head_lamp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_rear_door',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_rear_door_window',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_rear_fender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_rear_lamp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_rear_viewmirror',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_rear_wheel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='left_rear_window',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='rear_bumper',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='rear_seat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='rear_wind_screen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_front_door',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_front_door_window',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_front_fender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_front_seat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_front_wheel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_head_lamp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_rear_door',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_rear_door_window',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_rear_fender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_rear_lamp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_rear_viewmirror',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_rear_wheel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='right_rear_window',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='sound_system',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='steering',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='suspension',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='wind_screen',
            field=models.BooleanField(default=False),
        ),
    ]
