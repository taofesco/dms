from account.models import MyUser
from account.serializers import UserSerializer
import random
from datetime import datetime, timedelta



from django.http.response import JsonResponse
import time
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.generic import *
from rest_framework.views import APIView
from django.http import Http404

from rest_framework.response import Response
#from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.



# Create your views here.


class MainPage(View):
    def get(self, request):
        return render(request, "public.html")


class ActivationPage(View):
    def get(self, request):
        return render(request, "public.html")

# class MainPage(TemplateView):
#     template_name = "public.html"


class Error404(TemplateView):
    template_name = "public.html"


def error_404_view(request, exception):
    data = {"name": "Workstomer.com"}
    return render(request, 'myapp/error_404.html', data)


class ServiceWorker(TemplateView):
    template_name = "public/service-worker.js"
    content_type = 'application/javascript'
    name = "service-worker.js"


