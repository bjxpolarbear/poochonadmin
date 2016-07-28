# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.Client'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='quote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='quotes.Quote'),
        ),
    ]
