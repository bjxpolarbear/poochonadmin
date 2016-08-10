from django.db import models
from django.core.urlresolvers import reverse

from clients.models import Client
from quotes.models import Quote
from structure.models import JobStatus, Procedure, SampleType, SampleStatus, Organism


class Job(models.Model):

    job_id = models.AutoField(db_column='Job_ID', primary_key=True)
    job_name = models.CharField(db_column='Job_Name', max_length=45)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_submitted = models.DateField(db_column='Date_Submitted', blank=True, null=True)
    date_completed = models.DateField(db_column='Date_Completed', blank=True, null=True)
    # job_type = models.ForeignKey(JobType, db_column='Job_Type', on_delete=models.PROTECT)
    job_status = models.ForeignKey(JobStatus, db_column='Job_Status', on_delete=models.PROTECT)
    quote = models.ForeignKey(Quote, on_delete=models.SET_NULL, blank=True, null=True)

    procedures = models.ManyToManyField(Procedure)


    class Meta:
        permissions = (
            ("view_job", "Can view job"),
         )

    def __str__(self):
        return self.client.__str__() + ': ' + self.job_name

    def get_absolute_url(self):
        return reverse('jobs:detail', kwargs={'pk': self.pk})

    def fill_procedure(self):
        procedures = self.procedures.all()
        added_procedure = []    # Buffer for newly added procedures
        # filling the ancestors
        for procedure in procedures:
            ancestors = procedure.get_ancestors()
            for ancestor in ancestors:
                if ancestor not in procedures or added_procedure:
                    self.procedures.add(ancestor)
                    added_procedure.append(ancestor)


class Sample(models.Model):

    name = models.CharField(db_column='Name', max_length=255)
    description = models.TextField(db_column='Description', blank=True, null=True)
    sample_type = models.ForeignKey(SampleType, on_delete=models.PROTECT)
    organism = models.ForeignKey(Organism, on_delete=models.PROTECT)

    sample_status = models.ForeignKey(SampleStatus, on_delete=models.PROTECT)
    date_received = models.DateField(db_column='Date_Received', blank=True, null=True)
    location = models.CharField(db_column='Location', max_length=255)
    storage = models.CharField(db_column='Storage', max_length=255, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)#, related_name='sample_client')
    quote = models.ForeignKey(Quote, on_delete=models.PROTECT, blank=True, null=True)#, related_name='sample_quote')
    job = models.ForeignKey(Job, on_delete=models.PROTECT, blank=True, null=True, related_name='sample_job')

    class Meta:
        permissions = (
            ("view_sample", "Can view sample"),
        )

    def __str__(self):
        return self.client + ': ' + self.name
