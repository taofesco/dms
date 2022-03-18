import uuid
from datetime import date
from autoslug import AutoSlugField
import uuid
from django.core.checks import messages
from django.utils.text import slugify

from django.db import models
from account.models import MyUser

# Create your models here.


class Employee(models.Model):
    Technical = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    id = models.UUIDField(primary_key=True, blank=True,
                          default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        MyUser, null=True, on_delete=models.CASCADE, blank=True)
    is_admin = active = models.BooleanField(
        null=True, default=False, blank=True)
    technical = models.CharField(
        choices=Technical, max_length=20, null=True, blank=True)
    title = models.CharField(max_length=500, null=True)
    first_name = models.CharField(max_length=500, null=True)
    middle_name = models.CharField(max_length=500, null=True)
    last_name = models.CharField(max_length=500, null=True)
    designation = models.CharField(max_length=500, null=True)
    level = models.CharField(max_length=500, null=True)
    employee_no = models.CharField(max_length=500, null=True)
    position_management = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(null=True, default=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Budget(models.Model):
    year = models.IntegerField(null=True)
    annual_budget = models.IntegerField(null=True)
    #approraited_budget = models.IntegerField(null=True)
    preventive_maintenance = models.IntegerField( null=True)
    planned_maintenance = models.IntegerField( null=True)
    routine_maintenance = models.IntegerField( null=True)
    emergency_works = models.IntegerField(null=True)
    other_activities = models.IntegerField(null=True)
    released_budget = models.IntegerField( null=True)
    utilized_budget = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def approraited_budget(self):
        return int(self.preventive_maintenance) + int(self.planned_maintenance) + int(self.routine_maintenance) + int(self.emergency_works) + int(self.other_activities)

    def __str__(self):
        return '{} {}'.format(self.year, self.annual_budget)


class MaintenanceCost(models.Model):
    MODE = (
        ('Periodic', 'Periodic'),
        ('Routine', 'Routine'),
    )
    LEVEL = (
        ('Federal', 'Federal'),
        ('State', 'State'),
        ('LGA:Rural', 'LGA:Rural'),
        ('LGA:Urban', 'LGA:Urban'),
    )
    mode = models.CharField(
        choices=MODE, max_length=20, null=True, blank=True)
    level = models.CharField(
        choices=LEVEL, max_length=20, null=True, blank=True)
    dual_carriage_amount = models.IntegerField(null=True)
    dual_carriage_percent = models.IntegerField(null=True)
    single_carriage_amount = models.IntegerField(null=True)
    single_carriage_percent = models.IntegerField(null=True)
    earth_carriage_amount = models.IntegerField(null=True)
    earth_carriage_percent = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)









