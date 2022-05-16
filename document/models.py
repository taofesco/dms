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

    Role = (
        ('View', 'View'),
        ('Create', 'Create'),
        ('Admin', 'Admin'),
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
    photo = models.FileField(upload_to='employee/', null=True, blank=True)
    role = models.CharField(
        choices=Role, max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(null=True, default=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Budget(models.Model):
    year =  models.IntegerField(null=True)
    annual_budget =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    #approraited_budget =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    preventive_maintenance =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    planned_maintenance =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    routine_maintenance =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    correction_works = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    emergency_works = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    other_activities =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    released_budget =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    utilized_budget =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # @property
    # def approraited_budget(self):
    #     return int(self.preventive_maintenance) + int(self.planned_maintenance) + int(self.routine_maintenance) + int(self.emergency_works) + int(self.other_activities)

    def __str__(self):
        return '{} {}'.format(self.year, self.annual_budget)


class FederalMaintenanceCost(models.Model):
    MODE = (
        ('Periodic', 'Periodic'),
        ('Routine', 'Routine'),
        ('Corrective', 'Corrective'),
        ('Reactive', 'Reactive'),
        ('Emergency', 'Emergency'),
    )
    year = models.IntegerField(null=True)
    mode = models.CharField(
        choices=MODE, max_length=20, null=True, blank=True)
    dual_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dual_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class StateMaintenanceCost(models.Model):
    MODE = (
        ('Periodic', 'Periodic'),
        ('Routine', 'Routine'),
        ('Corrective', 'Corrective'),
        ('Reactive', 'Reactive'),
        ('Emergency', 'Emergency'),
    )
    year = models.IntegerField(null=True)
    mode = models.CharField(
        choices=MODE, max_length=20, null=True, blank=True)
    dual_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dual_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class UrbanMaintenanceCost(models.Model):
    MODE = (
        ('Periodic', 'Periodic'),
        ('Routine', 'Routine'),
        ('Corrective', 'Corrective'),
        ('Reactive', 'Reactive'),
        ('Emergency', 'Emergency'),
    )
    year = models.IntegerField(null=True)
    mode = models.CharField(
        choices=MODE, max_length=20, null=True, blank=True)
    dual_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dual_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class RuralMaintenanceCost(models.Model):
    MODE = (
        ('Periodic', 'Periodic'),
        ('Routine', 'Routine'),
        ('Corrective', 'Corrective'),
        ('Reactive', 'Reactive'),
        ('Emergency', 'Emergency'),
    )
    year = models.IntegerField(null=True)
    mode = models.CharField(
        choices=MODE, max_length=20, null=True, blank=True)
    dual_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dual_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class VillageMaintenanceCost(models.Model):
    MODE = (
        ('Periodic', 'Periodic'),
        ('Routine', 'Routine'),
        ('Corrective', 'Corrective'),
        ('Reactive', 'Reactive'),
        ('Emergency', 'Emergency'),
    )
    year = models.IntegerField(null=True)
    mode = models.CharField(
        choices=MODE, max_length=20, null=True, blank=True)
    dual_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dual_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    single_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth_carriage_percent =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class RoadMaintenanceImpact(models.Model):
    year = models.IntegerField(null=True)
    impact_plan = models.CharField(max_length=500, null=True)
    gdp_economy = models.CharField(max_length=500, null=True)
    climate_change = models.CharField(max_length=500, null=True)
    other_factors_1 = models.CharField(max_length=500, null=True, blank=True)
    other_factors_2 = models.CharField(max_length=500, null=True, blank=True)
    other_factors_3 = models.CharField(max_length=500, null=True, blank=True)
    other_factors_2 = models.CharField(max_length=500, null=True, blank=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class ManagementPlan(models.Model):
    year = models.IntegerField(null=True)
    strategic_plan = models.CharField(max_length=500, null=True)
    management_plan = models.CharField(max_length=500, null=True)
    business_plan = models.CharField(max_length=500, null=True)
    department_plan = models.CharField(max_length=500, null=True)
    agency_plan = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class RoadAsset(models.Model):
    year = models.IntegerField(null=True)
    asset = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=500, null=True)
    numbers =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    classes = models.CharField(max_length=500, null=True)
    value =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # rebuilding_cost =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # road_furniture_cost =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # roads = models.CharField(max_length=500, null=True)
    # bridges = models.CharField(max_length=500, null=True)
    # tolled = models.BooleanField(null=True, default=False)
    # consession = models.BooleanField(null=True, default=False)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class NonRoadAsset(models.Model):
    year = models.IntegerField(null=True)
    asset = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=500, null=True)
    numbers = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    classes = models.CharField(max_length=500, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # laboratories =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # facilities = models.CharField(max_length=500, null=True)
    #plant_equipment =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # asphalt_plant =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # graders =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # sundry_equipment =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # mini_asphalt =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # loader =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Stakeholder(models.Model):
    year = models.IntegerField(null=True)
    name = models.CharField(max_length=500, null=True)
    stake = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=500, null=True)
    survey = models.CharField(max_length=500, null=True)
    other = models.CharField(max_length=2000, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class PESTLE(models.Model):
    year = models.IntegerField(null=True)
    political = models.CharField(max_length=500, null=True)
    economic = models.CharField(max_length=500, null=True)
    social = models.CharField(max_length=500, null=True)
    technology = models.CharField(max_length=500, null=True)
    legal = models.CharField(max_length=500, null=True)
    environment = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class RoadInformation(models.Model):
    year = models.IntegerField(null=True)
    revenue_source = models.CharField(max_length=500, null=True)
    periodic_audit = models.BooleanField(null=True, default=False)
    external_audit = models.BooleanField(null=True, default=False)
    tolled_road =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_length_road_corridor =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    corridor_condition = models.CharField(max_length=500, null=True)
    secondary_road_lenght =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    secondary_road_propotion = models.CharField(max_length=500, null=True)
    unpaved_road_lenght =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    unpaved_road_condition = models.CharField(max_length=500, null=True)
    no_road_per_state =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    no_road_per_zone =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_length_per_state =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_length_per_zone =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    condition_federal_road = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class PBMC(models.Model):
    year = models.IntegerField(null=True)
    road = models.CharField(max_length=500, null=True)
    maintained_road = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    road_length =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cost_of_road =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    capacity_of_contractor = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class PublicPrivatePartnership(models.Model):
    year = models.IntegerField(null=True)
    legislative_for_ppp = models.CharField(max_length=500, null=True)
    dedicated_ppp = models.BooleanField(null=True, default=False)
    dedicated_ppp_ministry = models.CharField(max_length=500, null=True)
    no_ppp_road =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    length_ppp_road =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class CountryInformation(models.Model):
    year = models.IntegerField(null=True)
    fund = models.CharField(max_length=500, null=True)
    road_user = models.CharField(max_length=500, null=True)
    public_private = models.CharField(max_length=500, null=True)
    road_agency = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class ProjectMaintenanceWork(models.Model):
    year = models.IntegerField(null=True)
    project = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=1500, null=True)
    contract_no =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    contractor = models.CharField(max_length=500, null=True)
    contract_sum =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    amount_appropriated =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    release =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    amount_certified =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    amount_paid =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    outstanding_amount =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    compl =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    remark = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class RoadProject(models.Model):
    year = models.IntegerField(null=True)
    east_west = models.CharField(max_length=1500, null=True)
    location = models.CharField(max_length=1500, null=True)
    contract = models.CharField(max_length=1500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class NonRoadProject(models.Model):
    year = models.IntegerField(null=True)
    works =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    good_services =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    consultancy =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class InventoryRoad(models.Model):
    year = models.IntegerField(null=True)
    name = models.CharField(max_length=500, null=True)
    route_no =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_length = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    total_carriageway = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    cway_width =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    shoulder_width =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ac = models.CharField(max_length=500, null=True)
    sd =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sub_base = models.CharField(max_length=500, null=True)
    base = models.CharField(max_length=500, null=True)
    shoulder = models.CharField(max_length=500, null=True)
    good =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fair =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    poor =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    bad =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class WorkStream(models.Model):
    year = models.IntegerField(null=True)
    condition = models.CharField(max_length=500, null=True)
    road = models.CharField(max_length=500, null=True)
    length = models.IntegerField(null=True)
    ball_unit = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Legend(models.Model):
    year = models.IntegerField(null=True)
    asphaltic_concrete = models.CharField(max_length=500, null=True)
    # wc =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # bc =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sd =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    earth = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


# HMWH Mandate Performance

class KPI(models.Model):
    year = models.IntegerField(null=True)
    period = models.CharField(max_length=500, null=True)
    activity = models.CharField(max_length=500, null=True)
    kpi = models.CharField(max_length=500, null=True)
    baseline = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    target = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    achievement = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    financial = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    challenges = models.TextField(null=True)
    job_created =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    no_contractor =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Activities(models.Model):
    year = models.IntegerField(null=True)
    period = models.CharField(max_length=500, null=True)
    state = models.CharField(max_length=500, null=True)
    contractor_no =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    contract_sum =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    length_recovered_1 =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    length_recovered_2 =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    job_statistics = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class SummaryMaintenance(models.Model):
    year = models.IntegerField(null=True)
    state = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=500, null=True)
    project_id = models.CharField(max_length=500, null=True)
    contractor_name = models.CharField(max_length=500, null=True)
    date_award = models.DateField(null=True)
    date_commence = models.DateField(null=True)
    date_complete = models.DateField(null=True)
    contract_sum =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    compl = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    length_recovered =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    job_created =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Deliverables1(models.Model):
    deliverable_no = models.CharField(max_length=1500, null=True)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=1500, null=True)
    support = models.CharField(max_length=500, null=True)
    main_output = models.CharField(max_length=500, null=True)
    baseline = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    target = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    actual = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    perf = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q1_target = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q1_actual = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q1_perf = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q2_target = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q2_actual = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q2_perf = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q3_target = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q3_actual = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q3_perf = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    annual_target = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    challenges = models.TextField(null=True)
    recommendations = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Deliverables2(models.Model):
    deliverable_no = models.CharField(max_length=1500, null=True)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=1500, null=True)
    types = models.CharField(max_length=500, null=True)
    main_output = models.CharField(max_length=500, null=True)
    metric = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    baseline = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    target = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    actual = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    q1_target = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    q1_actual = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    q2_target = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    q2_actual = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    q3_target = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    q3_actual = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    q2_target = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    q2_actual = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    annual_target = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    annual_actual = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    source_data = models.TextField(null=True)
    agency = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class SummaryScorecard(models.Model):
    range = models.CharField(max_length=1500, null=True)
    year = models.IntegerField(null=True)
    length_recovered = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    q1 = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    q2 = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    q3 = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    q4 = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Folder(models.Model):
    MODE = (
        ('Project', 'Project'),
        ('Cost', 'Cost'),
        ('Inventory', 'Inventory'),
        ('Performance', 'Performance'),
        ('Scorecard', 'Scorecard'),
        ('External', 'External'),
        ('Media', 'Media'),
    )
    media_folder = models.CharField(max_length=500, choices=MODE, blank=True, null=True)
    name = models.CharField(max_length=500, unique=True, null=True)
    created_by = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, related_name='folder_created_by')
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class FolderFile(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True, related_name='folder_file')
    file = models.FileField(upload_to='files/')
    created_by = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, related_name='folder_file_created_by')
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class ImportFile(models.Model):
    file = models.FileField(upload_to='files/import')
    created_by = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, related_name='import_file_created_by')
    date_created = models.DateTimeField(auto_now_add=True, null=True)



