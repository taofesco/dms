from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View
from django.contrib.auth.views import FormView, LoginView, AuthenticationForm
from django.conf import settings
from django.utils.http import is_safe_url


from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from account.models import MyUser,EmailConfirmatiom



class ConfirmEmail(View):
    def get(self, request, token, *args, **kwargs):
        try:
            email_confirm = EmailConfirmatiom.objects.get(token=token)
        except EmailConfirmatiom.DoesNotExist:
            email_confirm = None
            success = False
        if email_confirm is not None:
            user = MyUser.objects.get(id=email_confirm.user)
            user.is_active = True
            user.save()
            email_confirm.delete()
            success = True
        return render(request, "account/confirm_email.html", context={'success': success})
        








