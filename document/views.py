from django.shortcuts import render
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
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

from account.models import *
from account.serializers import UserSerializer
from document.models import *
from document.serializers import *


class Login(APIView):
    def post(self, request, *args, **kwargs):
        cd = request.data
        user = authenticate(request,
                            username=cd['username'],
                            password=cd['password'])
        try:
            employee = Employee.objects.get(user=user)
        except Employee.DoesNotExist:
            employee = None
        if employee is not None:
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'username': str(user.username),
                })
            else:
                return Response({
                    "data": "Access Denied"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "data": "Wrong Username or Password"
            }, status=status.HTTP_400_BAD_REQUEST)
