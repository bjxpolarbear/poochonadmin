# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0001_initial'),
        ('clients', '0001_initial'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('quote_date', models.DateField(db_column='Quote_Date')),
                ('expire_date', models.DateField(db_column='Expire_Date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='quote_client', to='clients.Client')),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='structure.JobType')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='structure.PaymentTerm')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='structure.QuoteStatus')),
            ],
        ),
        migrations.CreateModel(
            name='QuoteProcedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure', models.ForeignKey(db_column='Procedure_ID', on_delete=django.db.models.deletion.PROTECT, to='structure.Procedure')),
                ('quote', models.ForeignKey(db_column='Job_ID', on_delete=django.db.models.deletion.CASCADE, to='quotes.Quote')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('date_received', models.DateField(blank=True, db_column='Date_Received', null=True)),
                ('location', models.CharField(db_column='Location', max_length=255)),
                ('storage', models.CharField(blank=True, db_column='Storage', max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sample_client', to='clients.Client')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sample_job', to='jobs.Job')),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='structure.Organism')),
                ('quote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sample_quote', to='quotes.Quote')),
                ('sample_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='structure.SampleStatus')),
                ('sample_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='structure.SampleType')),
            ],
        ),
    ]
