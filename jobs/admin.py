from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Job, JobProcedure, JobType, Procedure

# Register your models here.


admin.site.register(Job)
admin.site.register(JobType)
# admin.site.register(Procedure)
admin.site.register(JobProcedure)


class ProcedureAdmin(TreeAdmin):
    form = movenodeform_factory(Procedure)

admin.site.register(Procedure, ProcedureAdmin)