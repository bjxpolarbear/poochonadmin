from django.db import models
from clients import models as clients_models
from jobs import models as jobs_models

from structure.models import PaymentTerm, QuoteStatus, SampleType, SampleStatus, Organism


class Quote(models.Model):

    name = models.CharField(db_column='Name', max_length=255)
    client = models.ForeignKey(clients_models.Client, on_delete=models.PROTECT, related_name='quote_client')

    quote_date = models.DateField(db_column='Quote_Date')
    expire_date = models.DateField(db_column='Expire_Date')
    payment = models.ForeignKey(PaymentTerm, on_delete=models.PROTECT)
    status = models.ForeignKey(QuoteStatus, on_delete=models.PROTECT)

    job_type = models.ForeignKey(jobs_models.JobType, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ("view_quote", "Can view quote"),
        )

    def __str__(self):
        return self.client + ': ' + self.name


class Sample(models.Model):

    name = models.CharField(db_column='Name', max_length=255)
    description = models.TextField(db_column='Description', blank=True, null=True)
    sample_type = models.ForeignKey(SampleType, on_delete=models.PROTECT)
    organism = models.ForeignKey(Organism, on_delete=models.PROTECT)

    sample_status = models.ForeignKey(SampleStatus, on_delete=models.PROTECT)
    date_received = models.DateField(db_column='Date_Received', blank=True, null=True)
    location = models.CharField(db_column='Location', max_length=255)
    storage = models.CharField(db_column='Storage', max_length=255, blank=True, null=True)
    client = models.ForeignKey(clients_models.Client, on_delete=models.PROTECT)#, related_name='sample_client')
    quote = models.ForeignKey(Quote, on_delete=models.PROTECT, blank=True, null=True)#, related_name='sample_quote')
    job = models.ForeignKey(jobs_models.Job, on_delete=models.PROTECT, blank=True, null=True, related_name='sample_job')


    class Meta:
        permissions = (
            ("view_sample", "Can view sample"),
        )

    def __str__(self):
        return self.client + ': ' + self.name


class QuoteProcedure(models.Model):

    quote = models.ForeignKey(Quote, db_column='Job_ID', on_delete=models.CASCADE)
    procedure = models.ForeignKey(jobs_models.Procedure, db_column='Procedure_ID', on_delete=models.PROTECT)


    class Meta:
        permissions = (
            ("view_quoteprocedure", "Can view quoteprocedure"),
        )