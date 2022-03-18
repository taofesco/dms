
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

]
