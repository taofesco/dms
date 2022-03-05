
from django.urls import path, include
from django.conf.urls import handler404

from document.views import *


urlpatterns = [
    path('login/', Login.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls',
                                    namespace='password_reset')),

]


