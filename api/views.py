from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CompanySerializer,EmployeeSerializer
from .models import Company,Employee
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class CompanyAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            comp = Company.objects.get(company_id=id)
            serializer = CompanySerializer(comp)
            return Response(serializer.data)
        comp = Company.objects.all()
        serializer = CompanySerializer(comp,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk,format=None):
        id = pk
        comp = Company.objects.get(company_id=id)
        serializer = CompanySerializer(comp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated!"},status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        id=pk
        comp = Company.objects.get(company_id=id)
        serializer = CompanySerializer(comp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Created!"})
        return Response(serializer.errors,status=status.HTTP_206_PARTIAL_CONTENT)
    def delete(self,request,pk,format=None):
        id = pk
        comp = Company.objects.get(company_id=id)
        comp.delete()
        return Response({"msg":"Data Deleted"},status=status.HTTP_200_OK)
        
class EmployeeAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            emp = Employee.objects.get(add_company_id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        # import pdb;pdb.set_trace()
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk,format=None):
        id = pk
        emp = Employee.objects.get(add_company_id=id)
        serializer = EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated!"},status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        id =pk
        emp = Employee.objects.get(add_company_id=id)
        serializer = EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Created!"})
        return Response(serializer.errors,status=status.HTTP_206_PARTIAL_CONTENT)
    def delete(self,request,pk,format=None):
        id = pk
        emp = Employee.objects.get(add_company_id=id)
        emp.delete()
        return Response({"msg":"Data Deleted"},status=status.HTTP_200_OK)
        