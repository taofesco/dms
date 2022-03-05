
from django.urls import path, include
from django.conf.urls import handler404

from public.views import *


urlpatterns = [
    path('', MainPage.as_view(), name="index"),
    path('account_activation/', ActivationPage.as_view(), name="account_activation"),
    path('service-worker.js', MainPage.as_view(), name="service-worker.js"),

]

handler404 = 'public.views.error_404_view'
