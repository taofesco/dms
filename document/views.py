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
        serializer = NonRoadProjectSerializer(nonroadproject, data=request.data)
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
        serializer = SummaryMaintenanceSerializer(summary_maintenance, many=True)
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
        serializer = SummaryMaintenanceSerializer(summary_maintenance, data=request.data)
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


