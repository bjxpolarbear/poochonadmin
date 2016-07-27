from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Job, JobProcedure

# Register your models here.


admin.site.register(Job)

# #This is the mapping class between Job and Procedure, debug only
# admin.site.register(JobProcedure)