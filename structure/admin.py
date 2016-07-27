from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Procedure, SampleType, SampleStatus, Organism, PaymentTerm, QuoteStatus, ItemCategory, JobType, JobStatus
# Register your models here.


# admin.site.register(Procedure)
admin.site.register(SampleType)
admin.site.register(SampleStatus)
admin.site.register(Organism)
admin.site.register(PaymentTerm)
admin.site.register(QuoteStatus)
admin.site.register(ItemCategory)
admin.site.register(JobType)
admin.site.register(JobStatus)


class ProcedureAdmin(TreeAdmin):
    form = movenodeform_factory(Procedure)

admin.site.register(Procedure, ProcedureAdmin)