from rest_framework import serializers

from .models import Assignment, Area, Activity, Employee, Truck


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields=(
        'activity_fk',
        'employees',
        'trucks',
        'state',
    )


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields=(
        'id_Area',
        'name_Area',
    )


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields=(
        'area_fk',
        'description_Activity',
        'start_date',
        'end_date',
        'start_time',
        'end_time',
        'state',
    )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields=(
        'area_fk',
        'identification',
        'first_name',
        'last_name',
        'state',
        'user_With_Permissions',
    )


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields=(
        'code',
        'state',
    )