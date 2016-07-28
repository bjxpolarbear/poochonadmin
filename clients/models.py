from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Client(models.Model):
    clientid = models.AutoField(db_column='ClientID', primary_key=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=45)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=45)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='Customer ID', unique=True, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company = models.TextField(db_column='Company', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cell_phone = models.CharField(db_column='Cell_Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    work_phone = models.CharField(db_column='Work_Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    alt_phone = models.CharField(db_column='Alt_Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=25, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    poochon_rep = models.CharField(db_column='Poochon_Rep', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        permissions = (
            ("view_client", "Can view client"),
        )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('clients:detail', kwargs={'pk': self.pk})
