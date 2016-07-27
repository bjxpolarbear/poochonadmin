from django.db import models


# Create your models here.
class SampleType(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    def __str__(self):
        return self.name


class SampleStatus(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    def __str__(self):
        return self.name


class Organism(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    def __str__(self):
        return self.name


class PaymentTerm(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    def __str__(self):
        return self.name


class QuoteStatus(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    def __str__(self):
        return self.name


class ItemCategory(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active',default=True)

    def __str__(self):
        return self.name


class JobType(models.Model):

    job_type_id = models.AutoField(db_column='Job_Type_ID', primary_key=True)
    tag = models.CharField(db_column='Job_Tag', max_length=50)
    type = models.CharField(db_column='Job_Type_Name', max_length=255)
    note = models.TextField(db_column='Job_Note', blank=True, null=True)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    def __str__(self):
        return self.tag + ' ' + self.type


class JobStatus(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    def __str__(self):
        return self.name