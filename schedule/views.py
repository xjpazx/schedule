from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from rest_framework.viewsets import ModelViewSet

from schedule.forms import ActivityForm
import json

from schedule.models import Assignment, Area, Activity, Employee, Truck
from schedule.serializers import AssignmentSerializer, AreaSerializer, ActivitySerializer, EmployeeSerializer, \
    TruckSerializer


class ScheduleView(View):
    def post(self, request, *args, **kwargs):
        form = ActivityForm(request.POST)
        if form.is_valid():
            addform = form.save(commit=False)
            addform.save()
            return HttpResponse('{}', content_type='application/json')
        response = form.errors.as_json()

        return HttpResponse(response, content_type='application/json')


class AssignmentView(ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()


class AreaView(ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()


class ActivityView(ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


class EmployeeView(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class TruckView(ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()