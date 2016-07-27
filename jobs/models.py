from django.db import models
from django.core.urlresolvers import reverse
from treebeard.mp_tree import MP_Node

from clients.models import Client
from structure.models import JobType, JobStatus


class Job(models.Model):

    job_id = models.AutoField(db_column='Job_ID', primary_key=True)
    job_name = models.CharField(db_column='Job_Name', max_length=45)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_submitted = models.DateField(db_column='Date_Submitted', blank=True, null=True)
    date_completed = models.DateField(db_column='Date_Completed', blank=True, null=True)
    job_type = models.ForeignKey(JobType, db_column='Job_Type', on_delete=models.PROTECT)
    job_status = models.ForeignKey(JobStatus, db_column='Job_Status', on_delete=models.PROTECT)
    # sample_prep = models.ManyToOneRel

    def get_absolute_url(self):
        return reverse('jobs:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.client.__str__() + ': ' + self.job_name


class Procedure(MP_Node):
    procedure_id = models.AutoField(db_column='Procedure_ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)

    def __str__(self):
        return self.name

    def indented_name(self):
        full_name = ''
        full_name += '----' * (self.depth - 1)
        full_name += '>'

        return full_name + self.name


class JobProcedure(models.Model):

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.PROTECT)
