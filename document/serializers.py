from rest_framework import serializers
from document.models import *
from django.contrib.auth.password_validation import validate_password


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):

    approraited_budget = serializers.SerializerMethodField('get_approraited_budget')

    class Meta:
        model = Budget
        fields = '__all__'

    def get_approraited_budget(self, obj):
        return obj.preventive_maintenance + obj.planned_maintenance + obj.routine_maintenance + obj.emergency_works + obj.other_activities
