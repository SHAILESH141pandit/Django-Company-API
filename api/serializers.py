from rest_framework import serializers
from api.models import company, Employee

# Create serializers here.
class company_serializer(serializers.HyperlinkedModelSerializer):
    Company_id = serializers.ReadOnlyField()
    class Meta:
        model = company
        fields ='__all__'
 
class EmployeeSrializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = '__all__'