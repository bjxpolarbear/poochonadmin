from django.db import models
from clients import models as clients_models
# from jobs import models as jobs_models
# Create your models here.


class Quote(models.Model):

    quote_id = models.AutoField(db_column='Job_ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255, blank=False, null=True)
    client = models.ForeignKey(clients_models.Client, on_delete=models.PROTECT, related_name='quote_client')
    job_type = models.ForeignKey(clients_models.Client, on_delete=models.PROTECT)


class QuoteProcedure(models.Model):

    quote_id = models.ForeignKey(Quote, db_column='Job_ID', on_delete=models.CASCADE)
    # procedure_id = models.ForeignKey(jobs_models.Procedure, db_column='Procedure_ID', on_delete=models.PROTECT, related_name='quote_procedure_id')


