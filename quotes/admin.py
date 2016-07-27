from django.contrib import admin

from .models import Quote, Sample, QuoteProcedure
# Register your models here.


admin.site.register(Quote)
admin.site.register(Sample)

# This is the mapping class between Job and Procedure, debug only
# admin.site.register(QuoteProcedure)