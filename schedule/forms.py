# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from cuser.middleware import CuserMiddleware
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
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        if (CuserMiddleware.get_user().is_superuser!=True):
            id_area=CuserMiddleware.get_user().employee.area_fk_id
            self.fields['area_fk'].initial = models.Area.objects.filter(id=id_area)



    def clean(self):
        data = self.cleaned_data
        try:
            start_date = data['start_date']
            end_date = data['end_date']
        except:
            raise ValidationError('The start time and the end time must have the following format AAAA-MM-DD')
        if start_date > end_date:
             raise ValidationError('la fecha final es menor a la inicial')
        return data



class VistaFormAdmin(forms.ModelForm):
    class Meta:
        model = models.Vista
        fields = ['name']


# class Duplicate(forms.Form)


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
        js = ('/static/project/ajaxDjango.js', '/static/project/assignament.js',)

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['employees'].queryset = models.Employee.objects.all().order_by('first_name')
        self.fields['trucks'].queryset = models.Truck.objects.all().order_by('code')



def valedate_employe(valor):
    fechas = models.Activity.objects.filter(description_Activity=valor).values('start_date')[0]["start_date"].strftime(
        '%Y-%m-%d')
    asignaciones = models.Assignment.objects.filter(activity_fk__start_date=fechas)
    l = []
    for a in asignaciones:
        l.append(a.employees_().strip())
    return l
