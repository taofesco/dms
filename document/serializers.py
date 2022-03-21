from rest_framework import serializers
from document.models import *
from django.contrib.auth.password_validation import validate_password


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):

    approraited_budget = serializers.SerializerMethodField('get_approraited_budget')

    class Meta:
        model = Budget
        fields = '__all__'

    def get_approraited_budget(self, obj):
        return obj.preventive_maintenance + obj.planned_maintenance + obj.routine_maintenance + obj.emergency_works + obj.other_activities


class MaintenanceCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceCost
        fields = '__all__'


class RoadMaintenanceImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadMaintenanceImpact
        fields = '__all__'


class ManagementPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementPlan
        fields = '__all__'


class RoadAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadAsset
        fields = '__all__'


class NonRoadAssetSerializer(serializers.ModelSerializer):
    plant_equipment = serializers.SerializerMethodField('get_plant_equipment')

    class Meta:
        model = NonRoadAsset
        fields = '__all__'

    def get_plant_equipment(self, obj):
        return obj.asphalt_plant + obj.graders + obj.sundry_equipment + obj.mini_asphalt + obj.loader


class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = '__all__'


class PESTLESerializer(serializers.ModelSerializer):
    class Meta:
        model = PESTLE
        fields = '__all__'

        

