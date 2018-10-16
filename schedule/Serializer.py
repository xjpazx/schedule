from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Activity, Employee

class EmployeeSerializer(ModelSerializer):

    class Meta:
        model=Employee
        fields=('username',
			'identification',
			'first_name',
			'last_name',
                )

class ActivitySerializer(ModelSerializer):
    employees=EmployeeSerializer(many=True,read_only=True)

    class Meta:
        model=Activity
        fields=('vista','description_Activity','date','start_time','end_time','description_time','employees','trucks',)

