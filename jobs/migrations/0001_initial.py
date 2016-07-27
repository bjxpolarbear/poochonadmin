# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(db_column='Job_ID', primary_key=True, serialize=False)),
                ('job_name', models.CharField(db_column='Job_Name', max_length=45)),
                ('date_submitted', models.DateField(blank=True, db_column='Date_Submitted', null=True)),
                ('date_completed', models.DateField(blank=True, db_column='Date_Completed', null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.Client')),
                ('job_status', models.ForeignKey(db_column='Job_Status', on_delete=django.db.models.deletion.PROTECT, to='structure.JobStatus')),
                ('job_type', models.ForeignKey(db_column='Job_Type', on_delete=django.db.models.deletion.PROTECT, to='structure.JobType')),
            ],
        ),
        migrations.CreateModel(
            name='JobProcedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('procedure_id', models.AutoField(db_column='Procedure_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='jobprocedure',
            name='procedure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jobs.Procedure'),
        ),
    ]
