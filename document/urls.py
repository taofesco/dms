
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


]
