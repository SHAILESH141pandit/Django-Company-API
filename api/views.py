from django.shortcuts import render
from rest_framework import viewsets
from api.models import company, Employee
from api.serializers import company_serializer, EmployeeSrializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = company_serializer

    # This method defined for pass custom urls
    # componies/{componyId}/emplyees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            comp = company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=comp)
            emps_serializer = EmployeeSrializer(emps, many=True, context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Company might not exist | Error'
            })
            
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSrializer
