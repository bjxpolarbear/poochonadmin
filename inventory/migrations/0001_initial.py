# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('is_active', models.BooleanField(db_column='Is_Active', default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=1023)),
                ('item_id', models.CharField(blank=True, db_column='Item_ID', max_length=127, null=True, unique=True)),
                ('unit', models.CharField(db_column='Unit', max_length=63)),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('unit_price', models.FloatField(blank=True, db_column='Unit_Price', null=True)),
                ('date_received', models.DateField(blank=True, db_column='Date_Received', null=True)),
                ('location', models.CharField(db_column='Location', max_length=255)),
                ('sub_location', models.CharField(blank=True, db_column='Sub_Location', max_length=255, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Category')),
            ],
        ),
    ]
