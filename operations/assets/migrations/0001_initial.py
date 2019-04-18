# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-18 07:07
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import lib.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0023_auto_20180828_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('changed_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('category_one', models.CharField(blank=True, choices=[('appliances', 'Appliances'), ('electronic_equipment', 'Electronic Equipment'), ('furniture', 'Furniture'), ('it_equipment', 'IT Equipment'), ('stationery', 'Stationery')], max_length=50, null=True, verbose_name='Category 1')),
                ('category_two', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category 2')),
                ('category_three', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category 3')),
                ('asset_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Asset Description')),
                ('make', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Serial Number')),
                ('colour', models.CharField(blank=True, max_length=255, null=True)),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('condition', models.CharField(blank=True, choices=[('good', 'Good'), ('new', 'New'), ('poor', 'Poor')], max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('in_use', 'In Use'), ('in_storage', 'In Storage')], max_length=50, null=True)),
                ('supplier_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Supplier Name')),
                ('warranty_expiry', models.DateTimeField(blank=True, null=True, verbose_name='Warranty Expiry')),
                ('address', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='asset_address', to='operations.Address')),
            ],
            options={
                'default_permissions': [],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('changed_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('quantity', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, choices=[('administration', 'Administration'), ('client_services', 'Client Services'), ('finance', 'Finance'), ('human_resources', 'Human Resources'), ('it', 'IT'), ('marketing', 'Marketing'), ('operations', 'Operations'), ('sales', 'Sales')], max_length=50, null=True)),
                ('created_by', lib.fields.ProtectedForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_asset_detail', to=settings.AUTH_USER_MODEL)),
                ('district', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='district_asset_detail', to='operations.Branch')),
                ('modified_by', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_asset_detail', to=settings.AUTH_USER_MODEL)),
                ('region', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='region_asset_detail', to='operations.Region')),
            ],
            options={
                'default_permissions': [],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetPurchaseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('changed_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('invoice_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Invoice Number')),
                ('purchase_date', models.DateTimeField(blank=True, null=True, verbose_name='Purchase Date')),
                ('asset_purchase_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Purchase Price')),
                ('vat', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='VAT')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total Price')),
                ('created_by', lib.fields.ProtectedForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_purchase_detail_asset', to=settings.AUTH_USER_MODEL)),
                ('modified_by', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_purchase_detail_asset', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalAsset',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('changed_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('category_one', models.CharField(blank=True, choices=[('appliances', 'Appliances'), ('electronic_equipment', 'Electronic Equipment'), ('furniture', 'Furniture'), ('it_equipment', 'IT Equipment'), ('stationery', 'Stationery')], max_length=50, null=True, verbose_name='Category 1')),
                ('category_two', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category 2')),
                ('category_three', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category 3')),
                ('asset_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Asset Description')),
                ('make', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Serial Number')),
                ('colour', models.CharField(blank=True, max_length=255, null=True)),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('condition', models.CharField(blank=True, choices=[('good', 'Good'), ('new', 'New'), ('poor', 'Poor')], max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('in_use', 'In Use'), ('in_storage', 'In Storage')], max_length=50, null=True)),
                ('supplier_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Supplier Name')),
                ('warranty_expiry', models.DateTimeField(blank=True, null=True, verbose_name='Warranty Expiry')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('address', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='operations.Address')),
                ('asset_detail', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='assets.AssetDetail')),
                ('asset_purchase_detail', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='assets.AssetPurchaseDetail')),
                ('contact_person', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='operations.Contact')),
                ('created_by', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical asset',
            },
        ),
        migrations.CreateModel(
            name='HistoricalAssetDetail',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('changed_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('quantity', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, choices=[('administration', 'Administration'), ('client_services', 'Client Services'), ('finance', 'Finance'), ('human_resources', 'Human Resources'), ('it', 'IT'), ('marketing', 'Marketing'), ('operations', 'Operations'), ('sales', 'Sales')], max_length=50, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('district', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='operations.Branch')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('region', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='operations.Region')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical asset detail',
            },
        ),
        migrations.CreateModel(
            name='HistoricalAssetPurchaseDetail',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('changed_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('invoice_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Invoice Number')),
                ('purchase_date', models.DateTimeField(blank=True, null=True, verbose_name='Purchase Date')),
                ('asset_purchase_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Purchase Price')),
                ('vat', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='VAT')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total Price')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', lib.fields.ProtectedForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical asset purchase detail',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_detail',
            field=lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='asset_detail', to='assets.AssetDetail'),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_purchase_detail',
            field=lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='asset_purchase_detail', to='assets.AssetPurchaseDetail'),
        ),
        migrations.AddField(
            model_name='asset',
            name='contact_person',
            field=lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='asset_contact', to='operations.Contact'),
        ),
        migrations.AddField(
            model_name='asset',
            name='created_by',
            field=lib.fields.ProtectedForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_asset', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asset',
            name='modified_by',
            field=lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_asset', to=settings.AUTH_USER_MODEL),
        ),
    ]
