from rest_framework import serializers
from document.models import *
from django.contrib.auth.password_validation import validate_password


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):

    approraited_budget = serializers.SerializerMethodField(
        'get_approraited_budget')

    class Meta:
        model = Budget
        fields = '__all__'

    def get_approraited_budget(self, obj):
        return obj.preventive_maintenance + obj.planned_maintenance + obj.routine_maintenance + obj.emergency_works + obj.other_activities


class FederalMaintenanceCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FederalMaintenanceCost
        fields = '__all__'

class StateMaintenanceCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateMaintenanceCost
        fields = '__all__'


class UrbanMaintenanceCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrbanMaintenanceCost
        fields = '__all__'


class RuralMaintenanceCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuralMaintenanceCost
        fields = '__all__'


class VillageMaintenanceCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageMaintenanceCost
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

    # def get_plant_equipment(self, obj):
    #     return obj.asphalt_plant + obj.graders + obj.sundry_equipment + obj.mini_asphalt + obj.loader


class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = '__all__'


class PESTLESerializer(serializers.ModelSerializer):
    class Meta:
        model = PESTLE
        fields = '__all__'


class RoadInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadInformation
        fields = '__all__'


class PBMCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PBMC
        fields = '__all__'


class PublicPrivatePartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicPrivatePartnership
        fields = '__all__'


class ProjectMaintenanceWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMaintenanceWork
        fields = '__all__'


class CountryInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInformation
        fields = '__all__'


class RoadProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadProject
        fields = '__all__'


class NonRoadProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonRoadProject
        fields = '__all__'


class InventoryRoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryRoad
        fields = '__all__'


class WorkStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStream
        fields = '__all__'


class LegendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legend
        fields = '__all__'


class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = '__all__'


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'


class SummaryMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryMaintenance
        fields = '__all__'


class Deliverables1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverables1
        fields = '__all__'

class Deliverables2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverables2
        fields = '__all__'


class SummaryScorecardSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(
        'get_total')
    class Meta:
        model = SummaryScorecard
        fields = '__all__'

    def get_total(self, obj):
        return obj.q1 + obj.q2 + obj.q3 + obj.q4 



class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'


class FolderFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FolderFile
        fields = '__all__'


class ImportFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportFile
        fields = '__all__'



