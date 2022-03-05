from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import ConfirmEmail

urlpatterns = [
    # post views
    path("email_confirmation/<token>/", ConfirmEmail.as_view())
]
