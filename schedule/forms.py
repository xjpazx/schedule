# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError

from schedule import models
from django_select2.forms import *
import datetime


class ActivityForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = [
            'area_fk',
            'start_date',
            'end_date',
            'description_Activity',
            'start_time',
            'end_time',
            'state',

        ]

    class Media:
         js = ('/static/project/activity.js',)

    # def __init__(self, *args, **kwargs):
    #     super(ActivityForm, self).__init__(*args, **kwargs)
    #     self.fields['employees'].queryset = models.Employee.objects.all().order_by('first_name')
    #     self.fields['trucks'].queryset = models.Truck.objects.all().order_by('code')

    def clean(self):
        data = self.cleaned_data
        try:
            start_time = data['start_time']
            end_time = data['end_time']
        except:
            raise ValidationError('The start time and the end time must have the following format HH:MM')


class VistaFormAdmin(forms.ModelForm):
    class Meta:
        model = models.Vista
        fields = ['name']

#class Duplicate(forms.Form)


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = [
            'activity_fk',
            'employees',
            'trucks',
            'state',

        ]

    class Media:
        js = ('/static/project/assignament.js',)

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['employees'].queryset = models.Employee.objects.all().order_by('first_name')
        self.fields['trucks'].queryset = models.Truck.objects.all().order_by('code')

    def valedate_employe(self,valor):
        fechas = models.Activity.objects.filter(description_Activity=valor).values('start_date')[0]["start_date"].strftime('%Y-%m-%d')
        asignaciones=models.Assignment.objects.filter(activity_fk__start_date=fechas)
        l=[]
        for a in asignaciones:
            l.append(a.employees_())
        return l