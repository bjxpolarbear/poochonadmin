from django.contrib import admin

# Register your models here.
from .models import Job, JobProcedure, JobType, Procedure

admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(Procedure)
admin.site.register(JobProcedure)
