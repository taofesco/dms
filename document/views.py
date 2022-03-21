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


class EmployeeList(APIView):
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BudgetList(APIView):
    def get(self, request, format=None):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BudgetDetail(APIView):
    def get_object(self, pk):
        try:
            return Budget.objects.get(pk=pk)
        except Budget.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        budget = self.get_object(pk)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        budget = self.get_object(pk)
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        budget = self.get_object(pk)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoadMaintenanceImpactlist(APIView):
    def get(self, request, format=None):
        roadmaintenanceimpacts = RoadMaintenanceImpact.objects.all()
        serializer = RoadMaintenanceImpactSerializer(roadmaintenanceimpacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoadMaintenanceImpactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoadMaintenanceImpactDetail(APIView):
    def get_object(self, pk):
        try:
            return RoadMaintenanceImpact.objects.get(pk=pk)
        except RoadMaintenanceImpact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        roadmaintenanceimpact = self.get_object(pk)
        serializer = RoadMaintenanceImpactSerializer(roadmaintenanceimpact)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        roadmaintenanceimpact = self.get_object(pk)
        serializer = RoadMaintenanceImpactSerializer(roadmaintenanceimpact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        roadmaintenanceimpact = self.get_object(pk)
        roadmaintenanceimpact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManagementPlanList(APIView):
    def get(self, request, format=None):
        managementplans = ManagementPlan.objects.all()
        serializer = ManagementPlanSerializer(managementplans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ManagementPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManagementPlanDetail(APIView):
    def get_object(self, pk):
        try:
            return ManagementPlan.objects.get(pk=pk)
        except ManagementPlan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        managementplan = self.get_object(pk)
        serializer = ManagementPlanSerializer(managementplan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        managementplan = self.get_object(pk)
        serializer = ManagementPlanSerializer(managementplan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        managementplan = self.get_object(pk)
        managementplan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoadAssetList(APIView):
    def get(self, request, format=None):
        roadassets = RoadAsset.objects.all()
        serializer = RoadAssetSerializer(roadassets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoadAssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoadAssetDetail(APIView):
    def get_object(self, pk):
        try:
            return RoadAsset.objects.get(pk=pk)
        except RoadAsset.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        roadasset = self.get_object(pk)
        serializer = RoadAssetSerializer(roadasset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        roadasset = self.get_object(pk)
        serializer = RoadAssetSerializer(roadasset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        roadasset = self.get_object(pk)
        roadasset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NonRoadAssetList(APIView):
    def get(self, request, format=None):
        nonroadassets = NonRoadAsset.objects.all()
        serializer = NonRoadAssetSerializer(nonroadassets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NonRoadAssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NonRoadAssetDetail(APIView):
    def get_object(self, pk):
        try:
            return NonRoadAsset.objects.get(pk=pk)
        except NonRoadAsset.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        nonroadasset = self.get_object(pk)
        serializer = NonRoadAssetSerializer(nonroadasset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        nonroadasset = self.get_object(pk)
        serializer = NonRoadAssetSerializer(nonroadasset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        nonroadasset = self.get_object(pk)
        nonroadasset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StakeholderList(APIView):
    def get(self, request, format=None):
        stakeholders = Stakeholder.objects.all()
        serializer = StakeholderSerializer(stakeholders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StakeholderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StakeholderDetail(APIView):
    def get_object(self, pk):
        try:
            return Stakeholder.objects.get(pk=pk)
        except Stakeholder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stakeholder = self.get_object(pk)
        serializer = StakeholderSerializer(stakeholder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stakeholder = self.get_object(pk)
        serializer = StakeholderSerializer(stakeholder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stakeholder = self.get_object(pk)
        stakeholder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PESTLEList(APIView):
    def get(self, request, format=None):
        pestles = PESTLE.objects.all()
        serializer = PESTLESerializer(pestles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PESTLESerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PESTLEDetail(APIView):
    def get_object(self, pk):
        try:
            return PESTLE.objects.get(pk=pk)
        except PESTLE.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pestle = self.get_object(pk)
        serializer = PESTLESerializer(pestle)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pestle = self.get_object(pk)
        serializer = PESTLESerializer(pestle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pestle = self.get_object(pk)
        pestle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)