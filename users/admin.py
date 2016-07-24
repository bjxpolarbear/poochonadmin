from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User




# from .models import Employee


# # define an inline admin descripotor
# class EmployeeInline(admin.StackedInline):
#     model = Employee
#     can_delete = False
#     verbose_name_plural = 'employee'
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (EmployeeInline,)
#
#
#
# # Register your models here.
# admin.site.register(Employee)
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)