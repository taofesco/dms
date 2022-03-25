
from django.urls import path, include
from django.conf.urls import handler404

from document.views import *


urlpatterns = [
    path('login/', Login.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls',
                                    namespace='password_reset')),

    path('employee/', EmployeeList.as_view()),
    path('employee/<uuid:pk>/', EmployeeDetail.as_view()),
    path('budget/', BudgetList.as_view()),
    path('budget/<int:pk>/', BudgetDetail.as_view()),
    path('maintenance_impact/', RoadMaintenanceImpactlist.as_view()),
    path('maintenance_impact/<int:pk>/', RoadMaintenanceImpactDetail.as_view()),
    path('management_plan/', ManagementPlanList.as_view()),
    path('management_plan/<int:pk>/', ManagementPlanDetail.as_view()),
    path('road_asset/', RoadAssetList.as_view()),
    path('road_asset/<int:pk>/', RoadAssetDetail.as_view()),
    path('non_road_asset/', NonRoadAssetList.as_view()),
    path('non_road_asset/<int:pk>/', NonRoadAssetDetail.as_view()),
    path('stakeholder/', StakeholderList.as_view()),
    path('stakeholder/<int:pk>/', StakeholderDetail.as_view()),
    path('pestle/', PESTLEList.as_view()),
    path('pestle/<int:pk>/', PESTLEDetail.as_view()),
    path('road_information/', RoadInformationList.as_view()),
    path('road_information/<int:pk>/', RoadInformationDetail.as_view()),
    path('pbmc/', PBMCList.as_view()),
    path('pbmc/<int:pk>/', PBMCDetail.as_view()),
    path('public_private/', PublicPrivatePartnershipList.as_view()),
    path('public_private/<int:pk>/', PublicPrivatePartnershipDetail.as_view()),
    path('project_maintenance/', ProjectMaintenanceWorkList.as_view()),
    path('project_maintenance/<int:pk>/', ProjectMaintenanceWorkDetail.as_view()),
    path('road_project/', RoadProjectList.as_view()),
    path('road_project/<int:pk>/', RoadProjectDetail.as_view()),
    path('non_road_project/', NonRoadProjectList.as_view()),
    path('non_road_project/<int:pk>/', NonRoadProjectDetail.as_view()),
    path('inventory_road/', InventoryRoadList.as_view()),
    path('inventory_road/<int:pk>/', InventoryRoadDetail.as_view()),
    path('work_stream/', WorkStreamList.as_view()),
    path('work_stream/<int:pk>/', WorkStreamDetail.as_view()),
    path('legend/', LegendList.as_view()),
    path('legend/<int:pk>/', LegendDetail.as_view()),
    path('kpi/', KPIList.as_view()),
    path('kpi/<int:pk>/', KPIDetail.as_view()),
    path('activities/', ActivitiesList.as_view()),
    path('activities/<int:pk>/', ActivitiesDetail.as_view()),
    path('summary_maintenance/', SummaryMaintenanceList.as_view()),
    path('summary_maintenance/<int:pk>/', SummaryMaintenanceDetail.as_view()),
    path('deliverable_1/', Deliverables1List.as_view()),
    path('deliverable_1/<int:pk>/', Deliverables1Detail.as_view()),
    path('deliverable_2/', Deliverables2List.as_view()),
    path('deliverable_2/<int:pk>/', Deliverables2Detail.as_view()),
    path('summary_scorecard/', SummaryScorecardList.as_view()),

]
