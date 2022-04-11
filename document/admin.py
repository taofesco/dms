from django.contrib import admin
from document.models import *

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', )
    search_fields = ('first_name',)


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'preventive_maintenance', 'planned_maintenance', 'routine_maintenance', 'emergency_works', 'other_activities',)
    search_fields = ('date_created',)
