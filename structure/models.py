from django.db import models
from treebeard.mp_tree import MP_Node


class Procedure(MP_Node):
    procedure_id = models.AutoField(db_column='Procedure_ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)

    class Meta:
        permissions = (
            ("view_procedure", "Can view procedure"),
        )

    def __str__(self):
        return self.name

    def indented_name(self):
        full_name = ''
        full_name += '----' * (self.depth - 1)
        full_name += '>'

        return full_name + self.name

class Service(models.Model):

    tag = models.CharField(db_column='Service_Tag', max_length=63)
    name = models.CharField(db_column='Service_Name', max_length=255)
    price = models.FloatField(db_column='Price')
    non_profit_price = models.FloatField(db_column='None_Profit_Price', blank=True, null=True)
    SOP = models.CharField(db_column='SOP', max_length=63, blank=True, null=True)
    note = models.TextField(db_column='Service_Note', blank=True, null=True)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    procedures = models.ManyToManyField(Procedure)

    class Meta:
        permissions = (
            ("view_service", "Can view service"),
        )

    def __str__(self):
        return self.tag + ' ' + self.name

class ServicePackage(models.Model):

    tag = models.CharField(db_column='Service_Package_Tag', max_length=63)
    name = models.CharField(db_column='Service_Package_Name', max_length=255)
    price = models.FloatField(db_column='Price')
    non_profit_price = models.FloatField(db_column='None_Profit_Price', blank=True, null=True)
    note = models.TextField(db_column='Service_Package_Note', blank=True, null=True)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    services = models.ManyToManyField(Service)

    class Meta:
        permissions = (
            ("view_servicepackage", "Can view service package"),
        )

    def __str__(self):
        return self.tag + ' ' + self.name


class SampleType(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    class Meta:
        permissions = (
            ("view_sampletype", "Can view sampletype"),
        )

    def __str__(self):
        return self.name


class SampleStatus(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    class Meta:
        permissions = (
            ("view_samplestatus", "Can view samplestatus"),
        )

    def __str__(self):
        return self.name


class Organism(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    class Meta:
        permissions = (
            ("view_organism", "Can view organism"),
        )

    def __str__(self):
        return self.name


class PaymentTerm(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    class Meta:
        permissions = (
            ("view_paymentterm", "Can view paymentterm"),
        )

    def __str__(self):
        return self.name


class QuoteStatus(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    class Meta:
        permissions = (
            ("view_quotestatus", "Can view quotestatus"),
        )

    def __str__(self):
        return self.name


class ItemCategory(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    class Meta:
        permissions = (
            ("view_ItemCategory", "Can view ItemCategory"),
        )

    def __str__(self):
        return self.name


class OrderStatus(models.Model):

    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    class Meta:
        permissions = (
            ("view_orderstatus", "Can view orderstatus"),
        )

    def __str__(self):
        return self.name

class JobStatus(models.Model):
    name = models.CharField(db_column='Name', max_length=255)
    is_active = models.BooleanField(db_column='Is_Active', default=True)

    class Meta:
        permissions = (
            ("view_jobstatus", "Can view jobstatus"),
        )

    def __str__(self):
        return self.name
