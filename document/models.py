import numbers
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



class RoadMaintenanceImpact(models.Model):
    impact_plan = models.CharField(max_length=500, null=True)
    gdp_economy = models.CharField(max_length=500, null=True)
    climate_change = models.CharField(max_length=500, null=True)
    other_factors_1 = models.CharField(max_length=500, null=True, blank=True)
    other_factors_2 = models.CharField(max_length=500, null=True, blank=True)
    other_factors_3 = models.CharField(max_length=500, null=True, blank=True)
    other_factors_4 = models.CharField(max_length=500, null=True, blank=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class ManagementPlan(models.Model):
    strategic_plan = models.CharField(max_length=500, null=True)
    management_plan = models.CharField(max_length=500, null=True)
    business_plan = models.CharField(max_length=500, null=True)
    department_plan = models.CharField(max_length=500, null=True)
    agency_plan = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class RoadAsset(models.Model):
    name = models.CharField(max_length=500, null=True)
    numbers = models.IntegerField(null=True)
    classes = models.CharField(max_length=500, null=True)
    value = models.IntegerField(null=True)
    rebuilding_cost = models.IntegerField(null=True)
    road_furniture_cost = models.IntegerField(null=True)
    roads = models.CharField(max_length=500, null=True)
    bridges = models.CharField(max_length=500, null=True)
    tolled = models.BooleanField(null=True, default=False)
    consession = models.BooleanField(null=True, default=False)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class NonRoadAsset(models.Model):
    location = models.CharField(max_length=500, null=True)
    laboratories = models.IntegerField(null=True)
    facilities = models.CharField(max_length=500, null=True)
    #plant_equipment = models.IntegerField(null=True)
    asphalt_plant = models.IntegerField(null=True)
    graders = models.IntegerField(null=True)
    sundry_equipment = models.IntegerField(null=True)
    mini_asphalt = models.IntegerField(null=True)
    loader = models.IntegerField(null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Stakeholder(models.Model):
    name = models.CharField(max_length=500, null=True)
    stake = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=500, null=True)
    survey = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)



class PESTLE(models.Model):
    political = models.CharField(max_length=500, null=True)
    economic = models.CharField(max_length=500, null=True)
    social = models.CharField(max_length=500, null=True)
    technology = models.CharField(max_length=500, null=True)
    legal = models.CharField(max_length=500, null=True)
    environment = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class RoadInformantion(models.Model):
    revenue_source = models.CharField(max_length=500, null=True)
    periodic_audit = models.BooleanField(null=True, default=False)
    external_audit = models.BooleanField(null=True, default=False)
    tolled_road = models.IntegerField(null=True)
    total_length_road_corridor = models.IntegerField(null=True)
    corridor_condition = models.CharField(max_length=500, null=True)
    secondary_road_lenght = models.IntegerField(null=True)
    secondary_road_propotion = models.CharField(max_length=500, null=True)
    unpaved_road_lenght = models.IntegerField(null=True)
    unpaved_road_condition = models.CharField(max_length=500, null=True)
    no_road_per_state = models.IntegerField(null=True)
    no_road_per_zone = models.IntegerField(null=True)
    total_length_per_state = models.IntegerField(null=True)
    total_length_per_zone = models.IntegerField(null=True)
    condition_federal_road = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class PBMC(models.Model):
    maintained_road = models.IntegerField(null=True)
    road_length = models.IntegerField(null=True)
    cost_of_road = models.IntegerField(null=True)
    capacity_of_contractor = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class PublicPrivatePartnership(models.Model):
    legislative_for_ppp = models.CharField(max_length=500, null=True)
    dedicated_ppp = models.BooleanField(null=True, default=False)
    dedicated_ppp_ministry = models.CharField(max_length=500, null=True)
    no_ppp_road = models.IntegerField(null=True)
    length_ppp_road = models.IntegerField(null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)




