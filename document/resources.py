from import_export import resources
from document.models import *


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        exclude = ('id', 'date_created', 'active',)


class BudgetResource(resources.ModelResource):
    class Meta:
        model = Budget
        exclude = ('id','date_created')




