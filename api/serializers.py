from rest_framework import serializers
from .models import Company,Employee

class CompanySerializer(serializers.ModelSerializer):
    # company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = ['company_id','name','address','about']
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','email','address','phone','add_company']