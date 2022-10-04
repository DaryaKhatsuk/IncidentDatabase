from django.contrib import admin
from .models import Employees, IncidentDB


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'full_name', 'title', 'address', 'family_composition')
    list_filter = ('certificate', 'full_name')
    search_fields = ('certificate', 'full_name',)

@admin.register(IncidentDB)
class IncidentDB(admin.ModelAdmin):
    list_display = ('certificate', 'full_name', 'title', 'address', 'family_composition')
    list_filter = ('certificate', 'full_name')
    search_fields = ('certificate', 'full_name',)