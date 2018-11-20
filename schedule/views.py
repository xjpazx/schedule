from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from schedule.permissions import AssignmentPermissions,ActivityPermissions,EmployeePermissions,TruckPermissions

from schedule.forms import ActivityForm,AssignmentForm, valedate_employe
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


class AssignView(View):
    def post(self, request, *args, **kwargs):
        valor = request.POST.get('val')
        resp= valedate_employe(valor)
        return JsonResponse({'data':resp},status=200)


class AssignmentView(ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    permission_classes = (IsAuthenticated,AssignmentPermissions)


class AreaView(ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    permission_classes = (IsAuthenticated,)


class ActivityView(ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    permission_classes = (IsAuthenticated,ActivityPermissions)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid:
            if request.data['start_date'] > request.data['end_date']:
                return Response({"ERROR":"la fecha final es menor a la inicial"},status=status.HTTP_401_UNAUTHORIZED)
            else:
                serializer.save()
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class EmployeeView(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = (IsAuthenticated,EmployeePermissions)

class TruckView(ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()
    permission_classes = (IsAuthenticated,TruckPermissions)