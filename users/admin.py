from django.contrib import admin
from django.contrib.auth.models import Permission, ContentType

class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    fieldsets = [
        (None,          {'fields': ['name','codename']}),

    ]
    list_display = ('name', 'codename')

admin.site.register(Permission, PermissionAdmin)

