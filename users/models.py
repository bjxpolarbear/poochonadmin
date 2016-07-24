from django.db import models
from django.contrib.auth.models import User

'''
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(db_column='Title', max_length=45, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

'''

