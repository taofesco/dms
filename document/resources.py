from import_export import resources
from document.models import *


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        exclude = ('id', 'date_created', 'photo', 'active',)


class BudgetResource(resources.ModelResource):
    class Meta:
        model = Budget
        exclude = ('id','date_created')


class FederalMaintenanceCostResource(resources.ModelResource):
    class Meta:
        model = FederalMaintenanceCost
        exclude = ('id','date_created')

class StateMaintenanceCostResource(resources.ModelResource):
    class Meta:
        model = StateMaintenanceCost
        exclude = ('id','date_created')


class UrbanMaintenanceCostResource(resources.ModelResource):
    class Meta:
        model = UrbanMaintenanceCost
        exclude = ('id','date_created')


class RuralMaintenanceCostResource(resources.ModelResource):
    class Meta:
        model = RuralMaintenanceCost
        exclude = ('id','date_created')


class VillageMaintenanceCostResource(resources.ModelResource):
    class Meta:
        model = VillageMaintenanceCost
        exclude = ('id','date_created')


class RoadMaintenanceImpactResource(resources.ModelResource):
    class Meta:
        model = RoadMaintenanceImpact
        exclude = ('id','date_created')


class ManagementPlanResource(resources.ModelResource):
    class Meta:
        model = ManagementPlan
        exclude = ('id','date_created')


class RoadAssetResource(resources.ModelResource):
    class Meta:
        model = RoadAsset
        exclude = ('id','date_created')


class NonRoadAssetResource(resources.ModelResource):
    class Meta:
        model = NonRoadAsset
        exclude = ('id','date_created')


class StakeholderResource(resources.ModelResource):
    class Meta:
        model = Stakeholder
        exclude = ('id','date_created')


class PESTLEResource(resources.ModelResource):
    class Meta:
        model = PESTLE
        exclude = ('id','date_created')


class RoadInformationResource(resources.ModelResource):
    class Meta:
        model = RoadInformation
        exclude = ('id','date_created')


class PBMCResource(resources.ModelResource):
    class Meta:
        model = PBMC
        exclude = ('id','date_created')


class PublicPrivatePartnershipResource(resources.ModelResource):
    class Meta:
        model = PublicPrivatePartnership
        exclude = ('id','date_created')


class ProjectMaintenanceWorkResource(resources.ModelResource):
    class Meta:
        model = ProjectMaintenanceWork
        exclude = ('id','date_created')


class RoadProjectResource(resources.ModelResource):
    class Meta:
        model = RoadProject
        exclude = ('id','date_created')


class NonRoadProjectResource(resources.ModelResource):
    class Meta:
        model = NonRoadProject
        exclude = ('id','date_created')


class InventoryRoadResource(resources.ModelResource):
    class Meta:
        model = InventoryRoad
        exclude = ('id','date_created')


class WorkStreamResource(resources.ModelResource):
    class Meta:
        model = WorkStream
        exclude = ('id','date_created')


class LegendResource(resources.ModelResource):
    class Meta:
        model = Legend
        exclude = ('id','date_created')


class KPIResource(resources.ModelResource):
    class Meta:
        model = KPI
        exclude = ('id','date_created')


class ActivitiesResource(resources.ModelResource):
    class Meta:
        model = Activities
        exclude = ('id','date_created')


class SummaryMaintenanceResource(resources.ModelResource):
    class Meta:
        model = SummaryMaintenance
        exclude = ('id','date_created')


class Deliverables1Resource(resources.ModelResource):
    class Meta:
        model = Deliverables1
        exclude = ('id','date_created')


class Deliverables2Resource(resources.ModelResource):
    class Meta:
        model = Deliverables2
        exclude = ('id','date_created')


class SummaryScorecardResource(resources.ModelResource):
    class Meta:
        model = SummaryScorecard
        exclude = ('id','date_created')





