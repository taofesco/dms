from email import header
import os
import csv
from django.shortcuts import render
import random
from datetime import datetime, timedelta
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Sum
from tablib import Dataset
from django.core.files.storage import default_storage


from django.http.response import JsonResponse
from django.http import HttpResponse
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
from document.resources import *


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
                    'role': str(employee.role),
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
    parser_classes = (MultiPartParser, FormParser)

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
    parser_classes = (MultiPartParser, FormParser)

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


class StaffUser(APIView):

    def get(self, request, format=None):
        employee = Employee.objects.get(user=request.user)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class FederalMaintenanceCostList(APIView):
    def get(self, request, format=None):
        federal_maintenance_costs = FederalMaintenanceCost.objects.all()
        serializer = FederalMaintenanceCostSerializer(
            federal_maintenance_costs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FederalMaintenanceCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FederalMaintenanceCostDetail(APIView):
    def get_object(self, pk):
        try:
            return FederalMaintenanceCost.objects.get(pk=pk)
        except FederalMaintenanceCost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        federal_maintenance_cost = self.get_object(pk)
        serializer = FederalMaintenanceCostSerializer(federal_maintenance_cost)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        federal_maintenance_cost = self.get_object(pk)
        serializer = FederalMaintenanceCostSerializer(
            federal_maintenance_cost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        federal_maintenance_cost = self.get_object(pk)
        federal_maintenance_cost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StateMaintenanceCostList(APIView):
    def get(self, request, format=None):
        state_maintenance_costs = StateMaintenanceCost.objects.all()
        serializer = StateMaintenanceCostSerializer(
            state_maintenance_costs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StateMaintenanceCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateMaintenanceCostDetail(APIView):
    def get_object(self, pk):
        try:
            return StateMaintenanceCost.objects.get(pk=pk)
        except StateMaintenanceCost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        state_maintenance_cost = self.get_object(pk)
        serializer = StateMaintenanceCostSerializer(state_maintenance_cost)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        state_maintenance_cost = self.get_object(pk)
        serializer = StateMaintenanceCostSerializer(
            state_maintenance_cost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        state_maintenance_cost = self.get_object(pk)
        state_maintenance_cost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UrbanMaintenanceCostList(APIView):
    def get(self, request, format=None):
        urban_maintenance_costs = UrbanMaintenanceCost.objects.all()
        serializer = UrbanMaintenanceCostSerializer(
            urban_maintenance_costs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UrbanMaintenanceCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UrbanMaintenanceCostDetail(APIView):
    def get_object(self, pk):
        try:
            return UrbanMaintenanceCost.objects.get(pk=pk)
        except UrbanMaintenanceCost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        urban_maintenance_cost = self.get_object(pk)
        serializer = UrbanMaintenanceCostSerializer(urban_maintenance_cost)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        urban_maintenance_cost = self.get_object(pk)
        serializer = UrbanMaintenanceCostSerializer(
            urban_maintenance_cost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        urban_maintenance_cost = self.get_object(pk)
        urban_maintenance_cost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RuralMaintenanceCostList(APIView):
    def get(self, request, format=None):
        rural_maintenance_costs = RuralMaintenanceCost.objects.all()
        serializer = RuralMaintenanceCostSerializer(
            rural_maintenance_costs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RuralMaintenanceCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RuralMaintenanceCostDetail(APIView):
    def get_object(self, pk):
        try:
            return RuralMaintenanceCost.objects.get(pk=pk)
        except RuralMaintenanceCost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rural_maintenance_cost = self.get_object(pk)
        serializer = RuralMaintenanceCostSerializer(rural_maintenance_cost)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rural_maintenance_cost = self.get_object(pk)
        serializer = RuralMaintenanceCostSerializer(
            rural_maintenance_cost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rural_maintenance_cost = self.get_object(pk)
        rural_maintenance_cost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VillageMaintenanceCostList(APIView):
    def get(self, request, format=None):
        village_maintenance_costs = VillageMaintenanceCost.objects.all()
        serializer = VillageMaintenanceCostSerializer(
            village_maintenance_costs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VillageMaintenanceCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VillageMaintenanceCostDetail(APIView):
    def get_object(self, pk):
        try:
            return VillageMaintenanceCost.objects.get(pk=pk)
        except VillageMaintenanceCost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        village_maintenance_cost = self.get_object(pk)
        serializer = VillageMaintenanceCostSerializer(village_maintenance_cost)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        village_maintenance_cost = self.get_object(pk)
        serializer = VillageMaintenanceCostSerializer(
            village_maintenance_cost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        village_maintenance_cost = self.get_object(pk)
        village_maintenance_cost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FederalCostReport(APIView):
    def get(self, request, format=None):
        federal_routine = FederalMaintenanceCost.objects.filter(mode="Routine")
        federal_periodic = FederalMaintenanceCost.objects.filter(
            mode="Periodic")
        federal_corrective = FederalMaintenanceCost.objects.filter(
            mode="Corrective")
        federal_reactive = FederalMaintenanceCost.objects.filter(
            mode="Reactive")
        federal_emergency = FederalMaintenanceCost.objects.filter(
            mode="Emergency")

        federal_routine_dual_amount_sum = federal_routine.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        federal_routine_single_amount_sum = federal_routine.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        federal_routine_earth_amount_sum = federal_routine.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        federal_routine_dual_percent_sum = federal_routine.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        federal_routine_single_percent_sum = federal_routine.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        federal_routine_earth_percent_sum = federal_routine.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        federal_routine_total_amount_sum = federal_routine_dual_amount_sum + \
            federal_routine_single_amount_sum + \
            federal_routine_earth_amount_sum
        federal_routine_total_percent_sum = federal_routine_dual_percent_sum + \
            federal_routine_single_percent_sum + \
            federal_routine_earth_percent_sum

        federal_periodic_dual_amount_sum = federal_periodic.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        federal_periodic_single_amount_sum = federal_periodic.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        federal_periodic_earth_amount_sum = federal_periodic.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        federal_periodic_dual_percent_sum = federal_periodic.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        federal_periodic_single_percent_sum = federal_periodic.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        federal_periodic_earth_percent_sum = federal_periodic.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        federal_periodic_total_amount_sum = federal_periodic_dual_amount_sum + \
            federal_periodic_single_amount_sum + \
            federal_periodic_earth_amount_sum
        federal_periodic_total_percent_sum = federal_periodic_dual_percent_sum + \
            federal_periodic_single_percent_sum + \
            federal_periodic_earth_percent_sum

        federal_corrective_dual_amount_sum = federal_corrective.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        federal_corrective_single_amount_sum = federal_corrective.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        federal_corrective_earth_amount_sum = federal_corrective.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        federal_corrective_dual_percent_sum = federal_corrective.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        federal_corrective_single_percent_sum = federal_corrective.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        federal_corrective_earth_percent_sum = federal_corrective.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        federal_corrective_total_amount_sum = federal_corrective_dual_amount_sum + \
            federal_corrective_single_amount_sum + \
            federal_corrective_earth_amount_sum
        federal_corrective_total_percent_sum = federal_corrective_dual_percent_sum + \
            federal_corrective_single_percent_sum + \
            federal_corrective_earth_percent_sum

        federal_reactive_dual_amount_sum = federal_reactive.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        federal_reactive_single_amount_sum = federal_reactive.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        federal_reactive_earth_amount_sum = federal_reactive.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        federal_reactive_dual_percent_sum = federal_reactive.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        federal_reactive_single_percent_sum = federal_reactive.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        federal_reactive_earth_percent_sum = federal_reactive.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        federal_reactive_total_amount_sum = federal_reactive_dual_amount_sum + \
            federal_reactive_single_amount_sum + \
            federal_reactive_earth_amount_sum
        federal_reactive_total_percent_sum = federal_reactive_dual_percent_sum + \
            federal_reactive_single_percent_sum + \
            federal_reactive_earth_percent_sum

        federal_emergency_dual_amount_sum = federal_emergency.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        federal_emergency_single_amount_sum = federal_emergency.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        federal_emergency_earth_amount_sum = federal_emergency.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        federal_emergency_dual_percent_sum = federal_emergency.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        federal_emergency_single_percent_sum = federal_emergency.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        federal_emergency_earth_percent_sum = federal_emergency.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        federal_emergency_total_amount_sum = federal_emergency_dual_amount_sum + \
            federal_emergency_single_amount_sum + \
            federal_emergency_earth_amount_sum
        federal_emergency_total_percent_sum = federal_emergency_dual_percent_sum + \
            federal_emergency_single_percent_sum + \
            federal_emergency_earth_percent_sum

        federal_dual_amount_subtotal = federal_routine_dual_amount_sum + \
            federal_periodic_dual_amount_sum + \
            federal_corrective_dual_amount_sum + \
            federal_reactive_dual_amount_sum + \
            federal_emergency_dual_amount_sum
        federal_single_amount_subtotal = federal_routine_single_amount_sum + \
            federal_periodic_single_amount_sum + \
            federal_corrective_single_amount_sum + \
            federal_reactive_single_amount_sum + \
            federal_emergency_single_amount_sum
        federal_earth_amount_subtotal = federal_routine_earth_amount_sum + \
            federal_periodic_earth_amount_sum + \
            federal_corrective_earth_amount_sum + \
            federal_reactive_earth_amount_sum + \
            federal_emergency_earth_amount_sum
        federal_dual_percent_subtotal = federal_routine_dual_percent_sum + \
            federal_periodic_dual_percent_sum + \
            federal_corrective_dual_percent_sum + \
            federal_reactive_dual_percent_sum + \
            federal_emergency_dual_percent_sum
        federal_single_percent_subtotal = federal_routine_single_percent_sum + \
            federal_periodic_single_percent_sum + \
            federal_corrective_single_percent_sum + \
            federal_reactive_single_percent_sum + \
            federal_emergency_single_percent_sum
        federal_earth_percent_subtotal = federal_routine_earth_percent_sum + \
            federal_periodic_earth_percent_sum + \
            federal_corrective_earth_percent_sum + \
            federal_reactive_earth_percent_sum + \
            federal_emergency_earth_percent_sum
        federal_total_amount_subtotal = federal_dual_amount_subtotal + \
            federal_single_amount_subtotal + \
            federal_earth_amount_subtotal
        federal_total_percent_subtotal = federal_dual_percent_subtotal + \
            federal_single_percent_subtotal + \
            federal_earth_percent_subtotal

        # federal_dual_amount_subtotal = federal_routine_dual_amount_sum + \
        #     federal_periodic_dual_amount_sum
        # federal_single_amount_subtotal = federal_routine_single_amount_sum + \
        #     federal_periodic_single_amount_sum
        # federal_earth_amount_subtotal = federal_routine_earth_amount_sum + \
        #     federal_periodic_earth_amount_sum
        # federal_dual_percent_subtotal = federal_routine_dual_percent_sum + \
        #     federal_periodic_dual_percent_sum
        # federal_single_percent_subtotal = federal_routine_single_percent_sum + \
        #     federal_periodic_single_percent_sum
        # federal_earth_percent_subtotal = federal_routine_earth_percent_sum + \
        #     federal_periodic_earth_percent_sum
        # federal_total_amount_subtotal = federal_routine_total_amount_sum + \
        #     federal_periodic_total_amount_sum
        # federal_total_percent_subtotal = federal_routine_total_percent_sum + \
        #     federal_periodic_total_percent_sum

        return Response({
            "routine": {
                "dual_amount": federal_routine_dual_amount_sum,
                "single_amount": federal_routine_single_amount_sum,
                "earth_amount": federal_routine_earth_amount_sum,
                "dual_percent": federal_routine_dual_percent_sum,
                "single_percent": federal_routine_single_percent_sum,
                "earth_percent": federal_routine_earth_percent_sum,
                "total_amount": federal_routine_total_amount_sum,
                "total_percent": federal_routine_total_percent_sum
            },
            "periodic": {
                "dual_amount": federal_periodic_dual_amount_sum,
                "single_amount": federal_periodic_single_amount_sum,
                "earth_amount": federal_periodic_earth_amount_sum,
                "dual_percent": federal_periodic_dual_percent_sum,
                "single_percent": federal_periodic_single_percent_sum,
                "earth_percent": federal_periodic_earth_percent_sum,
                "total_amount": federal_periodic_total_amount_sum,
                "total_percent": federal_periodic_total_percent_sum
            },
            "corrective": {
                "dual_amount": federal_corrective_dual_amount_sum,
                "single_amount": federal_corrective_single_amount_sum,
                "earth_amount": federal_corrective_earth_amount_sum,
                "dual_percent": federal_corrective_dual_percent_sum,
                "single_percent": federal_corrective_single_percent_sum,
                "earth_percent": federal_corrective_earth_percent_sum,
                "total_amount": federal_corrective_total_amount_sum,
                "total_percent": federal_corrective_total_percent_sum
            },
            "reactive": {
                "dual_amount": federal_reactive_dual_amount_sum,
                "single_amount": federal_reactive_single_amount_sum,
                "earth_amount": federal_reactive_earth_amount_sum,
                "dual_percent": federal_reactive_dual_percent_sum,
                "single_percent": federal_reactive_single_percent_sum,
                "earth_percent": federal_reactive_earth_percent_sum,
                "total_amount": federal_reactive_total_amount_sum,
                "total_percent": federal_reactive_total_percent_sum
            },
            "emergency": {
                "dual_amount": federal_emergency_dual_amount_sum,
                "single_amount": federal_emergency_single_amount_sum,
                "earth_amount": federal_emergency_earth_amount_sum,
                "dual_percent": federal_emergency_dual_percent_sum,
                "single_percent": federal_emergency_single_percent_sum,
                "earth_percent": federal_emergency_earth_percent_sum,
                "total_amount": federal_emergency_total_amount_sum,
                "total_percent": federal_emergency_total_percent_sum
            },
            "subtotal": {
                "dual_amount": federal_dual_amount_subtotal,
                "single_amount": federal_single_amount_subtotal,
                "earth_amount": federal_earth_amount_subtotal,
                "dual_percent": federal_dual_percent_subtotal,
                "single_percent": federal_single_percent_subtotal,
                "earth_percent": federal_earth_percent_subtotal,
                "total_amount": federal_total_amount_subtotal,
                "total_percent": federal_total_percent_subtotal
            }
        })


class StateCostReport(APIView):
    def get(self, request, format=None):
        state_routine = StateMaintenanceCost.objects.filter(mode="Routine")
        state_periodic = StateMaintenanceCost.objects.filter(mode="Periodic")
        state_corrective = StateMaintenanceCost.objects.filter(
            mode="Corrective")
        state_reactive = StateMaintenanceCost.objects.filter(mode="Reactive")
        state_emergency = StateMaintenanceCost.objects.filter(mode="Emergency")

        state_routine_dual_amount_sum = state_routine.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        state_routine_single_amount_sum = state_routine.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        state_routine_earth_amount_sum = state_routine.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        state_routine_dual_percent_sum = state_routine.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        state_routine_single_percent_sum = state_routine.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        state_routine_earth_percent_sum = state_routine.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        state_routine_total_amount_sum = state_routine_dual_amount_sum + \
            state_routine_single_amount_sum + \
            state_routine_earth_amount_sum
        state_routine_total_percent_sum = state_routine_dual_percent_sum + \
            state_routine_single_percent_sum + \
            state_routine_earth_percent_sum

        state_periodic_dual_amount_sum = state_periodic.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        state_periodic_single_amount_sum = state_periodic.aggregate(Sum('single_carriage_amount'))[
            'single_carriage_amount__sum']
        state_periodic_earth_amount_sum = state_periodic.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        state_periodic_dual_percent_sum = state_periodic.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        state_periodic_single_percent_sum = state_periodic.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        state_periodic_earth_percent_sum = state_periodic.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        state_periodic_total_amount_sum = state_periodic_dual_amount_sum + \
            state_periodic_single_amount_sum + \
            state_periodic_earth_amount_sum
        state_periodic_total_percent_sum = state_periodic_dual_percent_sum + \
            state_periodic_single_percent_sum + \
            state_periodic_earth_percent_sum

        state_corrective_dual_amount_sum = state_corrective.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        state_corrective_single_amount_sum = state_corrective.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        state_corrective_earth_amount_sum = state_corrective.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        state_corrective_dual_percent_sum = state_corrective.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        state_corrective_single_percent_sum = state_corrective.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        state_corrective_earth_percent_sum = state_corrective.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        state_corrective_total_amount_sum = state_corrective_dual_amount_sum + \
            state_corrective_single_amount_sum + \
            state_corrective_earth_amount_sum
        state_corrective_total_percent_sum = state_corrective_dual_percent_sum + \
            state_corrective_single_percent_sum + \
            state_corrective_earth_percent_sum

        state_reactive_dual_amount_sum = state_reactive.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        state_reactive_single_amount_sum = state_reactive.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        state_reactive_earth_amount_sum = state_reactive.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        state_reactive_dual_percent_sum = state_reactive.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        state_reactive_single_percent_sum = state_reactive.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        state_reactive_earth_percent_sum = state_reactive.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        state_reactive_total_amount_sum = state_reactive_dual_amount_sum + \
            state_reactive_single_amount_sum + \
            state_reactive_earth_amount_sum
        state_reactive_total_percent_sum = state_reactive_dual_percent_sum + \
            state_reactive_single_percent_sum + \
            state_reactive_earth_percent_sum

        state_emergency_dual_amount_sum = state_emergency.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        state_emergency_single_amount_sum = state_emergency.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        state_emergency_earth_amount_sum = state_emergency.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        state_emergency_dual_percent_sum = state_emergency.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        state_emergency_single_percent_sum = state_emergency.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        state_emergency_earth_percent_sum = state_emergency.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        state_emergency_total_amount_sum = state_emergency_dual_amount_sum + \
            state_emergency_single_amount_sum + \
            state_emergency_earth_amount_sum
        state_emergency_total_percent_sum = state_emergency_dual_percent_sum + \
            state_emergency_single_percent_sum + \
            state_emergency_earth_percent_sum

        state_dual_amount_subtotal = state_routine_dual_amount_sum + \
            state_periodic_dual_amount_sum + \
            state_corrective_dual_amount_sum + \
            state_reactive_dual_amount_sum + \
            state_emergency_dual_amount_sum
        state_single_amount_subtotal = state_routine_single_amount_sum + \
            state_periodic_single_amount_sum + \
            state_corrective_single_amount_sum + \
            state_reactive_single_amount_sum + \
            state_emergency_single_amount_sum
        state_earth_amount_subtotal = state_routine_earth_amount_sum + \
            state_periodic_earth_amount_sum + \
            state_corrective_earth_amount_sum + \
            state_reactive_earth_amount_sum + \
            state_emergency_earth_amount_sum
        state_dual_percent_subtotal = state_routine_dual_percent_sum + \
            state_periodic_dual_percent_sum + \
            state_corrective_dual_percent_sum + \
            state_reactive_dual_percent_sum + \
            state_emergency_dual_percent_sum
        state_single_percent_subtotal = state_routine_single_percent_sum + \
            state_periodic_single_percent_sum + \
            state_corrective_single_percent_sum + \
            state_reactive_single_percent_sum + \
            state_emergency_single_percent_sum
        state_earth_percent_subtotal = state_routine_earth_percent_sum + \
            state_periodic_earth_percent_sum + \
            state_corrective_earth_percent_sum + \
            state_reactive_earth_percent_sum + \
            state_emergency_earth_percent_sum
        state_total_amount_subtotal = state_dual_amount_subtotal + \
            state_single_amount_subtotal + \
            state_earth_amount_subtotal
        state_total_percent_subtotal = state_dual_percent_subtotal + \
            state_single_percent_subtotal + \
            state_earth_percent_subtotal

        return Response({
            "routine": {
                "dual_amount": state_routine_dual_amount_sum,
                "single_amount": state_routine_single_amount_sum,
                "earth_amount": state_routine_earth_amount_sum,
                "dual_percent": state_routine_dual_percent_sum,
                "single_percent": state_routine_single_percent_sum,
                "earth_percent": state_routine_earth_percent_sum,
                "total_amount": state_routine_total_amount_sum,
                "total_percent": state_routine_total_percent_sum
            },
            "periodic": {
                "dual_amount": state_periodic_dual_amount_sum,
                "single_amount": state_periodic_single_amount_sum,
                "earth_amount": state_periodic_earth_amount_sum,
                "dual_percent": state_periodic_dual_percent_sum,
                "single_percent": state_periodic_single_percent_sum,
                "earth_percent": state_periodic_earth_percent_sum,
                "total_amount": state_periodic_total_amount_sum,
                "total_percent": state_periodic_total_percent_sum
            },
            "corrective": {
                "dual_amount": state_corrective_dual_amount_sum,
                "single_amount": state_corrective_single_amount_sum,
                "earth_amount": state_corrective_earth_amount_sum,
                "dual_percent": state_corrective_dual_percent_sum,
                "single_percent": state_corrective_single_percent_sum,
                "earth_percent": state_corrective_earth_percent_sum,
                "total_amount": state_corrective_total_amount_sum,
                "total_percent": state_corrective_total_percent_sum
            },
            "reactive": {
                "dual_amount": state_reactive_dual_amount_sum,
                "single_amount": state_reactive_single_amount_sum,
                "earth_amount": state_reactive_earth_amount_sum,
                "dual_percent": state_reactive_dual_percent_sum,
                "single_percent": state_reactive_single_percent_sum,
                "earth_percent": state_reactive_earth_percent_sum,
                "total_amount": state_reactive_total_amount_sum,
                "total_percent": state_reactive_total_percent_sum
            },
            "emergency": {
                "dual_amount": state_emergency_dual_amount_sum,
                "single_amount": state_emergency_single_amount_sum,
                "earth_amount": state_emergency_earth_amount_sum,
                "dual_percent": state_emergency_dual_percent_sum,
                "single_percent": state_emergency_single_percent_sum,
                "earth_percent": state_emergency_earth_percent_sum,
                "total_amount": state_emergency_total_amount_sum,
                "total_percent": state_emergency_total_percent_sum
            },
            "subtotal": {
                "dual_amount": state_dual_amount_subtotal,
                "single_amount": state_single_amount_subtotal,
                "earth_amount": state_earth_amount_subtotal,
                "dual_percent": state_dual_percent_subtotal,
                "single_percent": state_single_percent_subtotal,
                "earth_percent": state_earth_percent_subtotal,
                "total_amount": state_total_amount_subtotal,
                "total_percent": state_total_percent_subtotal
            }
        })


class RuralCostReport(APIView):
    def get(self, request):
        # !/usr/bin/env python3
        rural_routine = RuralMaintenanceCost.objects.filter(mode="Routine")
        rural_periodic = RuralMaintenanceCost.objects.filter(mode="Periodic")
        rural_corrective = RuralMaintenanceCost.objects.filter(
            mode="Corrective")
        rural_reactive = RuralMaintenanceCost.objects.filter(mode="Reactive")
        rural_emergency = RuralMaintenanceCost.objects.filter(mode="Emergency")

        rural_routine_dual_amount_sum = rural_routine.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        rural_routine_single_amount_sum = rural_routine.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        rural_routine_earth_amount_sum = rural_routine.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        rural_routine_dual_percent_sum = rural_routine.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        rural_routine_single_percent_sum = rural_routine.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        rural_routine_earth_percent_sum = rural_routine.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        rural_routine_total_amount_sum = rural_routine_dual_amount_sum + \
            rural_routine_single_amount_sum + \
            rural_routine_earth_amount_sum
        rural_routine_total_percent_sum = rural_routine_dual_percent_sum + \
            rural_routine_single_percent_sum + \
            rural_routine_earth_percent_sum

        rural_periodic_dual_amount_sum = rural_periodic.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        rural_periodic_single_amount_sum = rural_periodic.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        rural_periodic_earth_amount_sum = rural_periodic.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        rural_periodic_dual_percent_sum = rural_periodic.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        rural_periodic_single_percent_sum = rural_periodic.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        rural_periodic_earth_percent_sum = rural_periodic.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        rural_periodic_total_amount_sum = rural_periodic_dual_amount_sum + \
            rural_periodic_single_amount_sum + \
            rural_periodic_earth_amount_sum
        rural_periodic_total_percent_sum = rural_periodic_dual_percent_sum + \
            rural_periodic_single_percent_sum + \
            rural_periodic_earth_percent_sum

        rural_corrective_dual_amount_sum = rural_corrective.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        rural_corrective_single_amount_sum = rural_corrective.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        rural_corrective_earth_amount_sum = rural_corrective.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        rural_corrective_dual_percent_sum = rural_corrective.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        rural_corrective_single_percent_sum = rural_corrective.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        rural_corrective_earth_percent_sum = rural_corrective.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        rural_corrective_total_amount_sum = rural_corrective_dual_amount_sum + \
            rural_corrective_single_amount_sum + \
            rural_corrective_earth_amount_sum
        rural_corrective_total_percent_sum = rural_corrective_dual_percent_sum + \
            rural_corrective_single_percent_sum + \
            rural_corrective_earth_percent_sum

        rural_reactive_dual_amount_sum = rural_reactive.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        rural_reactive_single_amount_sum = rural_reactive.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        rural_reactive_earth_amount_sum = rural_reactive.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        rural_reactive_dual_percent_sum = rural_reactive.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        rural_reactive_single_percent_sum = rural_reactive.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        rural_reactive_earth_percent_sum = rural_reactive.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        rural_reactive_total_amount_sum = rural_reactive_dual_amount_sum + \
            rural_reactive_single_amount_sum + \
            rural_reactive_earth_amount_sum
        rural_reactive_total_percent_sum = rural_reactive_dual_percent_sum + \
            rural_reactive_single_percent_sum + \
            rural_reactive_earth_percent_sum

        rural_emergency_dual_amount_sum = rural_emergency.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        rural_emergency_single_amount_sum = rural_emergency.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        rural_emergency_earth_amount_sum = rural_emergency.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        rural_emergency_dual_percent_sum = rural_emergency.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        rural_emergency_single_percent_sum = rural_emergency.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        rural_emergency_earth_percent_sum = rural_emergency.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        rural_emergency_total_amount_sum = rural_emergency_dual_amount_sum + \
            rural_emergency_single_amount_sum + \
            rural_emergency_earth_amount_sum
        rural_emergency_total_percent_sum = rural_emergency_dual_percent_sum + \
            rural_emergency_single_percent_sum + \
            rural_emergency_earth_percent_sum

        rural_dual_amount_subtotal = rural_routine_dual_amount_sum + \
            rural_periodic_dual_amount_sum + \
            rural_corrective_dual_amount_sum + \
            rural_reactive_dual_amount_sum + \
            rural_emergency_dual_amount_sum
        rural_single_amount_subtotal = rural_routine_single_amount_sum + \
            rural_periodic_single_amount_sum + \
            rural_corrective_single_amount_sum + \
            rural_reactive_single_amount_sum + \
            rural_emergency_single_amount_sum
        rural_earth_amount_subtotal = rural_routine_earth_amount_sum + \
            rural_periodic_earth_amount_sum + \
            rural_corrective_earth_amount_sum + \
            rural_reactive_earth_amount_sum + \
            rural_emergency_earth_amount_sum

        rural_dual_percent_subtotal = rural_routine_dual_percent_sum + \
            rural_periodic_dual_percent_sum + \
            rural_corrective_dual_percent_sum + \
            rural_reactive_dual_percent_sum + \
            rural_emergency_dual_percent_sum
        rural_single_percent_subtotal = rural_routine_single_percent_sum + \
            rural_periodic_single_percent_sum + \
            rural_corrective_single_percent_sum + \
            rural_reactive_single_percent_sum + \
            rural_emergency_single_percent_sum
        rural_earth_percent_subtotal = rural_routine_earth_percent_sum + \
            rural_periodic_earth_percent_sum + \
            rural_corrective_earth_percent_sum + \
            rural_reactive_earth_percent_sum + \
            rural_emergency_earth_percent_sum
        rural_total_amount_subtotal = rural_routine_total_amount_sum + \
            rural_periodic_total_amount_sum + \
            rural_corrective_total_amount_sum + \
            rural_reactive_total_amount_sum + \
            rural_emergency_total_amount_sum
        rural_total_percent_subtotal = rural_routine_total_percent_sum + \
            rural_periodic_total_percent_sum + \
            rural_corrective_total_percent_sum + \
            rural_reactive_total_percent_sum + \
            rural_emergency_total_percent_sum

        return Response({
            "routine": {
                "dual_amount": rural_routine_dual_amount_sum,
                "single_amount": rural_routine_single_amount_sum,
                "earth_amount": rural_routine_earth_amount_sum,
                "dual_percent": rural_routine_dual_percent_sum,
                "single_percent": rural_routine_single_percent_sum,
                "earth_percent": rural_routine_earth_percent_sum,
                "total_amount": rural_routine_total_amount_sum,
                "total_percent": rural_routine_total_percent_sum
            },
            "periodic": {
                "dual_amount": rural_periodic_dual_amount_sum,
                "single_amount": rural_periodic_single_amount_sum,
                "earth_amount": rural_periodic_earth_amount_sum,
                "dual_percent": rural_periodic_dual_percent_sum,
                "single_percent": rural_periodic_single_percent_sum,
                "earth_percent": rural_periodic_earth_percent_sum,
                "total_amount": rural_periodic_total_amount_sum,
                "total_percent": rural_periodic_total_percent_sum
            },
            "corrective": {
                "dual_amount": rural_corrective_dual_amount_sum,
                "single_amount": rural_corrective_single_amount_sum,
                "earth_amount": rural_corrective_earth_amount_sum,
                "dual_percent": rural_corrective_dual_percent_sum,
                "single_percent": rural_corrective_single_percent_sum,
                "earth_percent": rural_corrective_earth_percent_sum,
                "total_amount": rural_corrective_total_amount_sum,
                "total_percent": rural_corrective_total_percent_sum
            },
            "reactive": {
                "dual_amount": rural_reactive_dual_amount_sum,
                "single_amount": rural_reactive_single_amount_sum,
                "earth_amount": rural_reactive_earth_amount_sum,
                "dual_percent": rural_reactive_dual_percent_sum,
                "single_percent": rural_reactive_single_percent_sum,
                "earth_percent": rural_reactive_earth_percent_sum,
                "total_amount": rural_reactive_total_amount_sum,
                "total_percent": rural_reactive_total_percent_sum
            },
            "emergency": {
                "dual_amount": rural_emergency_dual_amount_sum,
                "single_amount": rural_emergency_single_amount_sum,
                "earth_amount": rural_emergency_earth_amount_sum,
                "dual_percent": rural_emergency_dual_percent_sum,
                "single_percent": rural_emergency_single_percent_sum,
                "earth_percent": rural_emergency_earth_percent_sum,
                "total_amount": rural_emergency_total_amount_sum,
                "total_percent": rural_emergency_total_percent_sum
            },
            "subtotal": {
                "dual_amount": rural_dual_amount_subtotal,
                "single_amount": rural_single_amount_subtotal,
                "earth_amount": rural_earth_amount_subtotal,
                "dual_percent": rural_dual_percent_subtotal,
                "single_percent": rural_single_percent_subtotal,
                "earth_percent": rural_earth_percent_subtotal,
                "total_amount": rural_total_amount_subtotal,
                "total_percent": rural_total_percent_subtotal
            }
        })


class UrbanCostReport(APIView):
    def get(self, request):
        urban_routine = UrbanMaintenanceCost.objects.filter(mode="Routine")
        urban_periodic = UrbanMaintenanceCost.objects.filter(mode="Periodic")
        urban_corrective = UrbanMaintenanceCost.objects.filter(
            mode="Corrective")
        urban_reactive = UrbanMaintenanceCost.objects.filter(mode="Reactive")
        urban_emergency = UrbanMaintenanceCost.objects.filter(mode="Emergency")

        urban_routine_dual_amount_sum = urban_routine.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        urban_routine_single_amount_sum = urban_routine.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        urban_routine_earth_amount_sum = urban_routine.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        urban_routine_dual_percent_sum = urban_routine.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        urban_routine_single_percent_sum = urban_routine.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        urban_routine_earth_percent_sum = urban_routine.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        urban_routine_total_amount_sum = urban_routine_dual_amount_sum + \
            urban_routine_single_amount_sum + \
            urban_routine_earth_amount_sum
        urban_routine_total_percent_sum = urban_routine_dual_percent_sum + \
            urban_routine_single_percent_sum + \
            urban_routine_earth_percent_sum

        urban_periodic_dual_amount_sum = urban_periodic.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        urban_periodic_single_amount_sum = urban_periodic.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        urban_periodic_earth_amount_sum = urban_periodic.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        urban_periodic_dual_percent_sum = urban_periodic.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        urban_periodic_single_percent_sum = urban_periodic.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        urban_periodic_earth_percent_sum = urban_periodic.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        urban_periodic_total_amount_sum = urban_periodic_dual_amount_sum + \
            urban_periodic_single_amount_sum + \
            urban_periodic_earth_amount_sum
        urban_periodic_total_percent_sum = urban_periodic_dual_percent_sum + \
            urban_periodic_single_percent_sum + \
            urban_periodic_earth_percent_sum

        urban_corrective_dual_amount_sum = urban_corrective.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        urban_corrective_single_amount_sum = urban_corrective.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        urban_corrective_earth_amount_sum = urban_corrective.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        urban_corrective_dual_percent_sum = urban_corrective.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        urban_corrective_single_percent_sum = urban_corrective.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        urban_corrective_earth_percent_sum = urban_corrective.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        urban_corrective_total_amount_sum = urban_corrective_dual_amount_sum + \
            urban_corrective_single_amount_sum + \
            urban_corrective_earth_amount_sum
        urban_corrective_total_percent_sum = urban_corrective_dual_percent_sum + \
            urban_corrective_single_percent_sum + \
            urban_corrective_earth_percent_sum

        urban_reactive_dual_amount_sum = urban_reactive.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        urban_reactive_single_amount_sum = urban_reactive.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        urban_reactive_earth_amount_sum = urban_reactive.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        urban_reactive_dual_percent_sum = urban_reactive.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        urban_reactive_single_percent_sum = urban_reactive.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        urban_reactive_earth_percent_sum = urban_reactive.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        urban_reactive_total_amount_sum = urban_reactive_dual_amount_sum + \
            urban_reactive_single_amount_sum + \
            urban_reactive_earth_amount_sum
        urban_reactive_total_percent_sum = urban_reactive_dual_percent_sum + \
            urban_reactive_single_percent_sum + \
            urban_reactive_earth_percent_sum

        urban_emergency_dual_amount_sum = urban_emergency.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        urban_emergency_single_amount_sum = urban_emergency.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        urban_emergency_earth_amount_sum = urban_emergency.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        urban_emergency_dual_percent_sum = urban_emergency.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        urban_emergency_single_percent_sum = urban_emergency.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        urban_emergency_earth_percent_sum = urban_emergency.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        urban_emergency_total_amount_sum = urban_emergency_dual_amount_sum + \
            urban_emergency_single_amount_sum + \
            urban_emergency_earth_amount_sum
        urban_emergency_total_percent_sum = urban_emergency_dual_percent_sum + \
            urban_emergency_single_percent_sum + \
            urban_emergency_earth_percent_sum

        urban_dual_amount_subtotal = urban_routine_dual_amount_sum + \
            urban_periodic_dual_amount_sum + \
            urban_corrective_dual_amount_sum + \
            urban_reactive_dual_amount_sum + \
            urban_emergency_dual_amount_sum
        urban_single_amount_subtotal = urban_routine_single_amount_sum + \
            urban_periodic_single_amount_sum + \
            urban_corrective_single_amount_sum + \
            urban_reactive_single_amount_sum + \
            urban_emergency_single_amount_sum
        urban_earth_amount_subtotal = urban_routine_earth_amount_sum + \
            urban_periodic_earth_amount_sum + \
            urban_corrective_earth_amount_sum + \
            urban_reactive_earth_amount_sum + \
            urban_emergency_earth_amount_sum
        urban_dual_percent_subtotal = urban_routine_dual_percent_sum + \
            urban_periodic_dual_percent_sum + \
            urban_corrective_dual_percent_sum + \
            urban_reactive_dual_percent_sum + \
            urban_emergency_dual_percent_sum
        urban_single_percent_subtotal = urban_routine_single_percent_sum + \
            urban_periodic_single_percent_sum + \
            urban_corrective_single_percent_sum + \
            urban_reactive_single_percent_sum + \
            urban_emergency_single_percent_sum
        urban_earth_percent_subtotal = urban_routine_earth_percent_sum + \
            urban_periodic_earth_percent_sum + \
            urban_corrective_earth_percent_sum + \
            urban_reactive_earth_percent_sum + \
            urban_emergency_earth_percent_sum
        urban_total_amount_subtotal = urban_routine_total_amount_sum + \
            urban_periodic_total_amount_sum + \
            urban_corrective_total_amount_sum + \
            urban_reactive_total_amount_sum + \
            urban_emergency_total_amount_sum
        urban_total_percent_subtotal = urban_routine_total_percent_sum + \
            urban_periodic_total_percent_sum + \
            urban_corrective_total_percent_sum + \
            urban_reactive_total_percent_sum + \
            urban_emergency_total_percent_sum

        return Response({
            "routine": {
                "dual_amount": urban_routine_dual_amount_sum,
                "single_amount": urban_routine_single_amount_sum,
                "earth_amount": urban_routine_earth_amount_sum,
                "dual_percent": urban_routine_dual_percent_sum,
                "single_percent": urban_routine_single_percent_sum,
                "earth_percent": urban_routine_earth_percent_sum,
                "total_amount": urban_routine_total_amount_sum,
                "total_percent": urban_routine_total_percent_sum
            },
            "periodic": {
                "dual_amount": urban_periodic_dual_amount_sum,
                "single_amount": urban_periodic_single_amount_sum,
                "earth_amount": urban_periodic_earth_amount_sum,
                "dual_percent": urban_periodic_dual_percent_sum,
                "single_percent": urban_periodic_single_percent_sum,
                "earth_percent": urban_periodic_earth_percent_sum,
                "total_amount": urban_periodic_total_amount_sum,
                "total_percent": urban_periodic_total_percent_sum
            },
            "corrective": {
                "dual_amount": urban_corrective_dual_amount_sum,
                "single_amount": urban_corrective_single_amount_sum,
                "earth_amount": urban_corrective_earth_amount_sum,
                "dual_percent": urban_corrective_dual_percent_sum,
                "single_percent": urban_corrective_single_percent_sum,
                "earth_percent": urban_corrective_earth_percent_sum,
                "total_amount": urban_corrective_total_amount_sum,
                "total_percent": urban_corrective_total_percent_sum
            },
            "reactive": {
                "dual_amount": urban_reactive_dual_amount_sum,
                "single_amount": urban_reactive_single_amount_sum,
                "earth_amount": urban_reactive_earth_amount_sum,
                "dual_percent": urban_reactive_dual_percent_sum,
                "single_percent": urban_reactive_single_percent_sum,
                "earth_percent": urban_reactive_earth_percent_sum,
                "total_amount": urban_reactive_total_amount_sum,
                "total_percent": urban_reactive_total_percent_sum
            },
            "emergency": {
                "dual_amount": urban_emergency_dual_amount_sum,
                "single_amount": urban_emergency_single_amount_sum,
                "earth_amount": urban_emergency_earth_amount_sum,
                "dual_percent": urban_emergency_dual_percent_sum,
                "single_percent": urban_emergency_single_percent_sum,
                "earth_percent": urban_emergency_earth_percent_sum,
                "total_amount": urban_emergency_total_amount_sum,
                "total_percent": urban_emergency_total_percent_sum
            },
            "subtotal": {
                "dual_amount": urban_dual_amount_subtotal,
                "single_amount": urban_single_amount_subtotal,
                "earth_amount": urban_earth_amount_subtotal,
                "dual_percent": urban_dual_percent_subtotal,
                "single_percent": urban_single_percent_subtotal,
                "earth_percent": urban_earth_percent_subtotal,
                "total_amount": urban_total_amount_subtotal,
                "total_percent": urban_total_percent_subtotal
            }
        })


class VillageCostReport(APIView):
    def get(self, request, format=None):
        village_routine = VillageMaintenanceCost.objects.filter(mode="Routine")
        village_periodic = VillageMaintenanceCost.objects.filter(
            mode="Periodic")
        village_corrective = VillageMaintenanceCost.objects.filter(
            mode="Corrective")
        village_reactive = VillageMaintenanceCost.objects.filter(
            mode="Reactive")
        village_emergency = VillageMaintenanceCost.objects.filter(
            mode="Emergency")

        village_routine_dual_amount_sum = village_routine.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        village_routine_single_amount_sum = village_routine.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        village_routine_earth_amount_sum = village_routine.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        village_routine_dual_percent_sum = village_routine.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        village_routine_single_percent_sum = village_routine.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        village_routine_earth_percent_sum = village_routine.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        village_routine_total_amount_sum = village_routine_dual_amount_sum + \
            village_routine_single_amount_sum + \
            village_routine_earth_amount_sum
        village_routine_total_percent_sum = village_routine_dual_percent_sum + \
            village_routine_single_percent_sum + \
            village_routine_earth_percent_sum

        village_periodic_dual_amount_sum = village_periodic.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        village_periodic_single_amount_sum = village_periodic.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        village_periodic_earth_amount_sum = village_periodic.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        village_periodic_dual_percent_sum = village_periodic.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        village_periodic_single_percent_sum = village_periodic.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        village_periodic_earth_percent_sum = village_periodic.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        village_periodic_total_amount_sum = village_periodic_dual_amount_sum + \
            village_periodic_single_amount_sum + \
            village_periodic_earth_amount_sum
        village_periodic_total_percent_sum = village_periodic_dual_percent_sum + \
            village_periodic_single_percent_sum + \
            village_periodic_earth_percent_sum

        village_corrective_dual_amount_sum = village_corrective.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        village_corrective_single_amount_sum = village_corrective.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        village_corrective_earth_amount_sum = village_corrective.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        village_corrective_dual_percent_sum = village_corrective.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        village_corrective_single_percent_sum = village_corrective.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        village_corrective_earth_percent_sum = village_corrective.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        village_corrective_total_amount_sum = village_corrective_dual_amount_sum + \
            village_corrective_single_amount_sum + \
            village_corrective_earth_amount_sum
        village_corrective_total_percent_sum = village_corrective_dual_percent_sum + \
            village_corrective_single_percent_sum + \
            village_corrective_earth_percent_sum

        village_reactive_dual_amount_sum = village_reactive.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        village_reactive_single_amount_sum = village_reactive.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        village_reactive_earth_amount_sum = village_reactive.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        village_reactive_dual_percent_sum = village_reactive.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        village_reactive_single_percent_sum = village_reactive.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        village_reactive_earth_percent_sum = village_reactive.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        village_reactive_total_amount_sum = village_reactive_dual_amount_sum + \
            village_reactive_single_amount_sum + \
            village_reactive_earth_amount_sum
        village_reactive_total_percent_sum = village_reactive_dual_percent_sum + \
            village_reactive_single_percent_sum + \
            village_reactive_earth_percent_sum

        village_emergency_dual_amount_sum = village_emergency.aggregate(
            Sum('dual_carriage_amount'))['dual_carriage_amount__sum']
        village_emergency_single_amount_sum = village_emergency.aggregate(
            Sum('single_carriage_amount'))['single_carriage_amount__sum']
        village_emergency_earth_amount_sum = village_emergency.aggregate(
            Sum('earth_carriage_amount'))['earth_carriage_amount__sum']
        village_emergency_dual_percent_sum = village_emergency.aggregate(
            Sum('dual_carriage_percent'))['dual_carriage_percent__sum']
        village_emergency_single_percent_sum = village_emergency.aggregate(
            Sum('single_carriage_percent'))['single_carriage_percent__sum']
        village_emergency_earth_percent_sum = village_emergency.aggregate(
            Sum('earth_carriage_percent'))['earth_carriage_percent__sum']
        village_emergency_total_amount_sum = village_emergency_dual_amount_sum + \
            village_emergency_single_amount_sum + \
            village_emergency_earth_amount_sum
        village_emergency_total_percent_sum = village_emergency_dual_percent_sum + \
            village_emergency_single_percent_sum + \
            village_emergency_earth_percent_sum

        village_dual_amount_subtotal = village_routine_dual_amount_sum + \
            village_periodic_dual_amount_sum + \
            village_corrective_dual_amount_sum + \
            village_reactive_dual_amount_sum + \
            village_emergency_dual_amount_sum
        village_single_amount_subtotal = village_routine_single_amount_sum + \
            village_periodic_single_amount_sum + \
            village_corrective_single_amount_sum + \
            village_reactive_single_amount_sum + \
            village_emergency_single_amount_sum
        village_earth_amount_subtotal = village_routine_earth_amount_sum + \
            village_periodic_earth_amount_sum + \
            village_corrective_earth_amount_sum + \
            village_reactive_earth_amount_sum + \
            village_emergency_earth_amount_sum
        village_dual_percent_subtotal = village_routine_dual_percent_sum + \
            village_periodic_dual_percent_sum + \
            village_corrective_dual_percent_sum + \
            village_reactive_dual_percent_sum + \
            village_emergency_dual_percent_sum

        village_single_percent_subtotal = village_routine_single_percent_sum + \
            village_periodic_single_percent_sum + \
            village_corrective_single_percent_sum + \
            village_reactive_single_percent_sum + \
            village_emergency_single_percent_sum
        village_earth_percent_subtotal = village_routine_earth_percent_sum + \
            village_periodic_earth_percent_sum + \
            village_corrective_earth_percent_sum + \
            village_reactive_earth_percent_sum + \
            village_emergency_earth_percent_sum

        village_total_amount_subtotal = village_routine_total_amount_sum + \
            village_periodic_total_amount_sum + \
            village_corrective_total_amount_sum + \
            village_reactive_total_amount_sum + \
            village_emergency_total_amount_sum
        village_total_percent_subtotal = village_routine_total_percent_sum + \
            village_periodic_total_percent_sum + \
            village_corrective_total_percent_sum + \
            village_reactive_total_percent_sum + \
            village_emergency_total_percent_sum

        return Response({
            "routine": {
                "dual_amount": village_routine_dual_amount_sum,
                "single_amount": village_routine_single_amount_sum,
                "earth_amount": village_routine_earth_amount_sum,
                "dual_percent": village_routine_dual_percent_sum,
                "single_percent": village_routine_single_percent_sum,
                "earth_percent": village_routine_earth_percent_sum,
                "total_amount": village_routine_total_amount_sum,
                "total_percent": village_routine_total_percent_sum
            },
            "periodic": {
                "dual_amount": village_periodic_dual_amount_sum,
                "single_amount": village_periodic_single_amount_sum,
                "earth_amount": village_periodic_earth_amount_sum,
                "dual_percent": village_periodic_dual_percent_sum,
                "single_percent": village_periodic_single_percent_sum,
                "earth_percent": village_periodic_earth_percent_sum,
                "total_amount": village_periodic_total_amount_sum,
                "total_percent": village_periodic_total_percent_sum
            },
            "corrective": {
                "dual_amount": village_corrective_dual_amount_sum,
                "single_amount": village_corrective_single_amount_sum,
                "earth_amount": village_corrective_earth_amount_sum,
                "dual_percent": village_corrective_dual_percent_sum,
                "single_percent": village_corrective_single_percent_sum,
                "earth_percent": village_corrective_earth_percent_sum,
                "total_amount": village_corrective_total_amount_sum,
                "total_percent": village_corrective_total_percent_sum
            },
            "reactive": {
                "dual_amount": village_reactive_dual_amount_sum,
                "single_amount": village_reactive_single_amount_sum,
                "earth_amount": village_reactive_earth_amount_sum,
                "dual_percent": village_reactive_dual_percent_sum,
                "single_percent": village_reactive_single_percent_sum,
                "earth_percent": village_reactive_earth_percent_sum,
                "total_amount": village_reactive_total_amount_sum,
                "total_percent": village_reactive_total_percent_sum
            },
            "emergency": {
                "dual_amount": village_emergency_dual_amount_sum,
                "single_amount": village_emergency_single_amount_sum,
                "earth_amount": village_emergency_earth_amount_sum,
                "dual_percent": village_emergency_dual_percent_sum,
                "single_percent": village_emergency_single_percent_sum,
                "earth_percent": village_emergency_earth_percent_sum,
                "total_amount": village_emergency_total_amount_sum,
                "total_percent": village_emergency_total_percent_sum
            },


            "subtotal": {
                "dual_amount": village_dual_amount_subtotal,
                "single_amount": village_single_amount_subtotal,
                "earth_amount": village_earth_amount_subtotal,
                "dual_percent": village_dual_percent_subtotal,
                "single_percent": village_single_percent_subtotal,
                "earth_percent": village_earth_percent_subtotal,
                "total_amount": village_total_amount_subtotal,
                "total_percent": village_total_percent_subtotal
            }
        })


class BudgetChart(APIView):
    def get(self, request, format=None):
        year = request.GET.get('year')
        if year and year != '' and year != 'undefined' and year != 'null':
            year = int(year)
            budgets = Budget.objects.filter(year__lte=year).order_by('year')[:10]
            serializer = BudgetSerializer(budgets, many=True)
            return Response(serializer.data)
        else:
            year = int(datetime.now().year)
            budgets = Budget.objects.filter(year__lte=year).order_by('year')[:10]
            serializer = BudgetSerializer(budgets, many=True)
            return Response(serializer.data)


class KPIChart(APIView):
    def get(self, request, format=None):
        year = request.GET.get('year')
        if year and year != '' and year != 'undefined' and year != 'null':
            year = int(year)
            kpis = KPI.objects.filter(year__lte=year).order_by('year')[:10]
            serializer = KPISerializer(kpis, many=True)
            return Response(serializer.data)
        else:
            year = int(datetime.now().year)
            kpis = KPI.objects.filter(year__lte=year).order_by('year')[:10]
            serializer = KPISerializer(kpis, many=True)
            return Response(serializer.data)



class BudgetList(APIView):
    def get(self, request, format=None):
        budgets = Budget.objects.all().order_by('-year')
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
        serializer = RoadMaintenanceImpactSerializer(
            roadmaintenanceimpacts, many=True)
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
        serializer = RoadMaintenanceImpactSerializer(
            roadmaintenanceimpact, data=request.data)
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
        serializer = ManagementPlanSerializer(
            managementplan, data=request.data)
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


class RoadInformationList(APIView):
    def get(self, request, format=None):
        roadinformations = RoadInformation.objects.all()
        serializer = RoadInformationSerializer(roadinformations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoadInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoadInformationDetail(APIView):
    def get_object(self, pk):
        try:
            return RoadInformation.objects.get(pk=pk)
        except RoadInformation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        roadinformation = self.get_object(pk)
        serializer = RoadInformationSerializer(roadinformation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        roadinformation = self.get_object(pk)
        serializer = RoadInformationSerializer(
            roadinformation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        roadinformation = self.get_object(pk)
        roadinformation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PBMCList(APIView):
    def get(self, request, format=None):
        pbmcs = PBMC.objects.all()
        serializer = PBMCSerializer(pbmcs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PBMCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PBMCDetail(APIView):
    def get_object(self, pk):
        try:
            return PBMC.objects.get(pk=pk)
        except PBMC.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pbmc = self.get_object(pk)
        serializer = PBMCSerializer(pbmc)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pbmc = self.get_object(pk)
        serializer = PBMCSerializer(pbmc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pbmc = self.get_object(pk)
        pbmc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublicPrivatePartnershipList(APIView):
    def get(self, request, format=None):
        publicprivatepartnerships = PublicPrivatePartnership.objects.all()
        serializer = PublicPrivatePartnershipSerializer(
            publicprivatepartnerships, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PublicPrivatePartnershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicPrivatePartnershipDetail(APIView):
    def get_object(self, pk):
        try:
            return PublicPrivatePartnership.objects.get(pk=pk)
        except PublicPrivatePartnership.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        publicprivatepartnership = self.get_object(pk)
        serializer = PublicPrivatePartnershipSerializer(
            publicprivatepartnership)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        publicprivatepartnership = self.get_object(pk)
        serializer = PublicPrivatePartnershipSerializer(
            publicprivatepartnership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        publicprivatepartnership = self.get_object(pk)
        publicprivatepartnership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CountryInformationList(APIView):
    def get(self, request, format=None):
        countryinformations = CountryInformation.objects.all()
        serializer = CountryInformationSerializer(
            countryinformations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountryInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryInformationDetail(APIView):
    def get_object(self, pk):
        try:
            return CountryInformation.objects.get(pk=pk)
        except CountryInformation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        countryinformation = self.get_object(pk)
        serializer = CountryInformationSerializer(countryinformation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        countryinformation = self.get_object(pk)
        serializer = CountryInformationSerializer(
            countryinformation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        countryinformation = self.get_object(pk)
        countryinformation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectMaintenanceWorkList(APIView):
    def get(self, request, format=None):
        projectmaintenanceworks = ProjectMaintenanceWork.objects.all()
        serializer = ProjectMaintenanceWorkSerializer(
            projectmaintenanceworks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectMaintenanceWorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectMaintenanceWorkDetail(APIView):
    def get_object(self, pk):
        try:
            return ProjectMaintenanceWork.objects.get(pk=pk)
        except ProjectMaintenanceWork.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        projectmaintenancework = self.get_object(pk)
        serializer = ProjectMaintenanceWorkSerializer(
            projectmaintenancework)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        projectmaintenancework = self.get_object(pk)
        serializer = ProjectMaintenanceWorkSerializer(
            projectmaintenancework, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        projectmaintenancework = self.get_object(pk)
        projectmaintenancework.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoadProjectList(APIView):
    def get(self, request, format=None):
        roadprojects = RoadProject.objects.all()
        serializer = RoadProjectSerializer(roadprojects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoadProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoadProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return RoadProject.objects.get(pk=pk)
        except RoadProject.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        roadproject = self.get_object(pk)
        serializer = RoadProjectSerializer(roadproject)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        roadproject = self.get_object(pk)
        serializer = RoadProjectSerializer(roadproject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        roadproject = self.get_object(pk)
        roadproject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NonRoadProjectList(APIView):
    def get(self, request, format=None):
        nonroadprojects = NonRoadProject.objects.all()
        serializer = NonRoadProjectSerializer(nonroadprojects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NonRoadProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NonRoadProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return NonRoadProject.objects.get(pk=pk)
        except NonRoadProject.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        nonroadproject = self.get_object(pk)
        serializer = NonRoadProjectSerializer(nonroadproject)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        nonroadproject = self.get_object(pk)
        serializer = NonRoadProjectSerializer(
            nonroadproject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        nonroadproject = self.get_object(pk)
        nonroadproject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InventoryRoadList(APIView):
    def get(self, request, format=None):
        inventoryroads = InventoryRoad.objects.all()
        serializer = InventoryRoadSerializer(inventoryroads, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InventoryRoadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryRoadDetail(APIView):
    def get_object(self, pk):
        try:
            return InventoryRoad.objects.get(pk=pk)
        except InventoryRoad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        inventoryroad = self.get_object(pk)
        serializer = InventoryRoadSerializer(inventoryroad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        inventoryroad = self.get_object(pk)
        serializer = InventoryRoadSerializer(inventoryroad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        inventoryroad = self.get_object(pk)
        inventoryroad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkStreamList(APIView):
    def get(self, request, format=None):
        workstreams = WorkStream.objects.all()
        serializer = WorkStreamSerializer(workstreams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkStreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkStreamDetail(APIView):
    def get_object(self, pk):
        try:
            return WorkStream.objects.get(pk=pk)
        except WorkStream.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        workstream = self.get_object(pk)
        serializer = WorkStreamSerializer(workstream)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        workstream = self.get_object(pk)
        serializer = WorkStreamSerializer(workstream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workstream = self.get_object(pk)
        workstream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LegendList(APIView):
    def get(self, request, format=None):
        legends = Legend.objects.all()
        serializer = LegendSerializer(legends, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LegendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LegendDetail(APIView):
    def get_object(self, pk):
        try:
            return Legend.objects.get(pk=pk)
        except Legend.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        legend = self.get_object(pk)
        serializer = LegendSerializer(legend)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        legend = self.get_object(pk)
        serializer = LegendSerializer(legend, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        legend = self.get_object(pk)
        legend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class KPIList(APIView):
    def get(self, request, format=None):
        kpis = KPI.objects.all()
        serializer = KPISerializer(kpis, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KPIDetail(APIView):
    def get_object(self, pk):
        try:
            return KPI.objects.get(pk=pk)
        except KPI.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        kpi = self.get_object(pk)
        serializer = KPISerializer(kpi)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        kpi = self.get_object(pk)
        serializer = KPISerializer(kpi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        kpi = self.get_object(pk)
        kpi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActivitiesList(APIView):
    def get(self, request, format=None):
        activities = Activities.objects.all()
        serializer = ActivitiesSerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActivitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivitiesDetail(APIView):
    def get_object(self, pk):
        try:
            return Activities.objects.get(pk=pk)
        except Activities.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitiesSerializer(activity)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitiesSerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SummaryMaintenanceList(APIView):
    def get(self, request, format=None):
        summary_maintenance = SummaryMaintenance.objects.all()
        serializer = SummaryMaintenanceSerializer(
            summary_maintenance, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SummaryMaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SummaryMaintenanceDetail(APIView):
    def get_object(self, pk):
        try:
            return SummaryMaintenance.objects.get(pk=pk)
        except SummaryMaintenance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        summary_maintenance = self.get_object(pk)
        serializer = SummaryMaintenanceSerializer(summary_maintenance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        summary_maintenance = self.get_object(pk)
        serializer = SummaryMaintenanceSerializer(
            summary_maintenance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        summary_maintenance = self.get_object(pk)
        summary_maintenance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Deliverables1List(APIView):
    def get(self, request, format=None):
        deliverables1 = Deliverables1.objects.all()
        serializer = Deliverables1Serializer(deliverables1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Deliverables1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Deliverables1Detail(APIView):
    def get_object(self, pk):
        try:
            return Deliverables1.objects.get(pk=pk)
        except Deliverables1.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        deliverables1 = self.get_object(pk)
        serializer = Deliverables1Serializer(deliverables1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        deliverables1 = self.get_object(pk)
        serializer = Deliverables1Serializer(deliverables1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        deliverables1 = self.get_object(pk)
        deliverables1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Deliverables2List(APIView):
    def get(self, request, format=None):
        deliverables2 = Deliverables2.objects.all()
        serializer = Deliverables2Serializer(deliverables2, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Deliverables2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Deliverables2Detail(APIView):
    def get_object(self, pk):
        try:
            return Deliverables2.objects.get(pk=pk)
        except Deliverables2.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        deliverables2 = self.get_object(pk)
        serializer = Deliverables2Serializer(deliverables2)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        deliverables2 = self.get_object(pk)
        serializer = Deliverables2Serializer(deliverables2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        deliverables2 = self.get_object(pk)
        deliverables2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SummaryScorecardList(APIView):
    def get(self, request, format=None):
        summary_scorecard = SummaryScorecard.objects.all()
        serializer = SummaryScorecardSerializer(summary_scorecard, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SummaryScorecardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SummaryScorecardDetail(APIView):
    def get_object(self, pk):
        try:
            return SummaryScorecard.objects.get(pk=pk)
        except SummaryScorecard.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        summary_scorecard = self.get_object(pk)
        serializer = SummaryScorecardSerializer(summary_scorecard)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        summary_scorecard = self.get_object(pk)
        serializer = SummaryScorecardSerializer(
            summary_scorecard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        summary_scorecard = self.get_object(pk)
        summary_scorecard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FolderList(APIView):

    def get(self, request, format=None):
        folder = Folder.objects.all()
        serializer = FolderSerializer(folder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        employee = Employee.objects.get(user=request.user)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectFolderList(APIView):

    def get(self, request, format=None):
        folder = Folder.objects.filter(media_folder='Project')
        serializer = FolderSerializer(folder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        employee = Employee.objects.get(user=request.user)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CostFolderList(APIView):

    def get(self, request, format=None):
        folder = Folder.objects.filter(media_folder='Cost')
        serializer = FolderSerializer(folder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        employee = Employee.objects.get(user=request.user)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryFolderList(APIView):

    def get(self, request, format=None):
        folder = Folder.objects.filter(media_folder='Inventory')
        serializer = FolderSerializer(folder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        employee = Employee.objects.get(user=request.user)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerformanceFolderList(APIView):

    def get(self, request, format=None):
        folder = Folder.objects.filter(media_folder='Performance')
        serializer = FolderSerializer(folder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        employee = Employee.objects.get(user=request.user)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScorecardFolderList(APIView):
    def get(self, request, format=None):
        folder = Folder.objects.filter(media_folder='Scorecard')
        serializer = FolderSerializer(folder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        employee = Employee.objects.get(user=request.user)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExternalFolderList(APIView):
    def get(self, request, format=None):
        folder = Folder.objects.filter(media_folder='External')
        serializer = FolderSerializer(folder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        employee = Employee.objects.get(user=request.user)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MediaFolderList(APIView):
    def get(self, request, format=None):
        folder = Folder.objects.filter(media_folder='Media')
        serializer = FolderSerializer(folder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        employee = Employee.objects.get(user=request.user)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=employee)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class FolderDetail(APIView):

    def get_object(self, pk):
        try:
            return Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        folder = self.get_object(pk)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        folder = self.get_object(pk)

        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        folder = self.get_object(pk)
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetFolder(APIView):

    def get_object(self, folder_name):
        try:
            return Folder.objects.get(name=folder_name)
        except Folder.DoesNotExist:
            raise Http404

    def get(self, request, folder_name, format=None):
        folder = self.get_object(folder_name)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)


class FolderFileList(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, folder_name, format=None):
        folder = Folder.objects.get(name=folder_name)
        folder_file = FolderFile.objects.filter(folder=folder)
        serializer = FolderFileSerializer(folder_file, many=True)
        return Response(serializer.data)

    def post(self, request, folder_name, format=None):
        employee = Employee.objects.get(user=request.user)
        folder = Folder.objects.get(name=folder_name)
        serializer = FolderFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=employee, folder=folder)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FolderFileDetail(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def get_object(self, pk):
        try:
            return FolderFile.objects.get(pk=pk)
        except FolderFile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        folder_file = self.get_object(pk)
        serializer = FolderFileSerializer(folder_file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        folder_file = self.get_object(pk)
        serializer = FolderFileSerializer(folder_file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        folder_file = self.get_object(pk)
        folder_file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" Import/Export  """


class EmployeeExport(APIView):
    def get(self, request, format=None):
        employee_resource = EmployeeResource()
        dataset = employee_resource.export()
        response = HttpResponse(
            dataset.csv, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="employee.xlsx"'
        return response


class BudgetImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        budget_resource = BudgetResource()
        dataset = budget_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="budget.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=Budget)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FederalMaintenanceCostImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        federal_maintenance_cost_resource = FederalMaintenanceCostResource()
        dataset = federal_maintenance_cost_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="federal_maintenance_cost.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=FederalMaintenanceCost)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateMaintenanceCostImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        state_maintenance_cost_resource = StateMaintenanceCostResource()
        dataset = state_maintenance_cost_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="state_maintenance_cost.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=StateMaintenanceCost)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UrbanMaintenanceCostImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        urban_maintenance_cost_resource = UrbanMaintenanceCostResource()
        dataset = urban_maintenance_cost_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="urban_maintenance_cost.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=UrbanMaintenanceCost)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RuralMaintenanceCostImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        rural_maintenance_cost_resource = RuralMaintenanceCostResource()
        dataset = rural_maintenance_cost_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="rural_maintenance_cost.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=RuralMaintenanceCost)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VillageMaintenanceCostImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        village_maintenance_cost_resource = VillageMaintenanceCostResource()
        dataset = village_maintenance_cost_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="village_maintenance_cost.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=VillageMaintenanceCost)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoadMaintenanceImpactImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        road_maintenance_impact_resource = RoadMaintenanceImpactResource()
        dataset = road_maintenance_impact_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="road_maintenance_impact.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=RoadMaintenanceImpact)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagementPlanImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        management_plan_resource = ManagementPlanResource()
        dataset = management_plan_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="management_plan.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=ManagementPlan)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoadAssetImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        road_asset_resource = RoadAssetResource()
        dataset = road_asset_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="road_asset.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=RoadAsset)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NonRoadAssetImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        non_road_asset_resource = NonRoadAssetResource()
        dataset = non_road_asset_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="non_road_asset.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=NonRoadAsset)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StakeholderImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        stakeholder_resource = StakeholderResource()
        dataset = stakeholder_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="stakeholder.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=Stakeholder)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PESTLEImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        pestle_resource = PESTLEResource()
        dataset = pestle_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="pestle.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=PESTLE)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoadInformationImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        road_information_resource = RoadInformationResource()
        dataset = road_information_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="road_information.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=RoadInformation)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PBMCImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        pbmc_resource = PBMCResource()
        dataset = pbmc_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="pbmc.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=PBMC)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicPrivatePartnershipImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        public_private_partnership_resource = PublicPrivatePartnershipResource()
        dataset = public_private_partnership_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="public_private_partnership.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=PublicPrivatePartnership)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryInformationImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        country_information_resource = CountryInformationResource()
        dataset = country_information_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="country_information.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=CountryInformation)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectMaintenanceWorkImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        project_maintenance_work_resource = ProjectMaintenanceWorkResource()
        dataset = project_maintenance_work_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="project_maintenance_work.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=ProjectMaintenanceWork)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoadProjectImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        road_project_resource = RoadProjectResource()
        dataset = road_project_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="road_project.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=RoadProject)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NonRoadProjectImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        non_road_project_resource = NonRoadProjectResource()
        dataset = non_road_project_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="non_road_project.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=NonRoadProject)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryRoadImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        inventory_road_resource = InventoryRoadResource()
        dataset = inventory_road_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="inventory_road.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=InventoryRoad)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkStreamImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        work_stream_resource = WorkStreamResource()
        dataset = work_stream_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="work_stream.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=WorkStream)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LegendImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        legend_resource = LegendResource()
        dataset = legend_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="legend.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=Legend)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KPIImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        kpi_resource = KPIResource()
        dataset = kpi_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="kpi.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=KPI)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivitiesImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        activities_resource = ActivitiesResource()
        dataset = activities_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="activities.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=Activities)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SummaryMaintenanceImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        summary_maintenance_resource = SummaryMaintenanceResource()
        dataset = summary_maintenance_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="summary_maintenance.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=SummaryMaintenance)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Deliverables1ImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        deliverables1_resource = Deliverables1Resource()
        dataset = deliverables1_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="deliverables1.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=Deliverables1)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Deliverables2ImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        deliverables2_resource = Deliverables2Resource()
        dataset = deliverables2_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="deliverables2.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(model=Deliverables2)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SummaryScorecardImportExport(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        summary_scorecard_resource = SummaryScorecardResource()
        dataset = summary_scorecard_resource.export()
        response = HttpResponse(
            dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="summary_scorecard.xlsx"'
        return response

    def post(self, request, format=None):
        book_resource = resources.modelresource_factory(
            model=SummaryScorecard)()
        serializer = ImportFileSerializer(data=request.data)
        if serializer.is_valid():
            import_file = serializer.save()
            dataset = Dataset().load(import_file.file.read())
            result = book_resource.import_data(
                dataset, format='xlsx',  dry_run=True)
            if not result.has_errors():
                result = book_resource.import_data(
                    dataset, format='xlsx', dry_run=False)
                import_file.delete()
                return Response({'Successful'}, status=status.HTTP_201_CREATED)
            else:
                import_file.delete()
                return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
