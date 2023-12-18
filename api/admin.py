from django.contrib import admin
from .models import Company,Employee

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id','name','address','type']
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','gender','add_company']