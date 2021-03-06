# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError

from schedule import models
from django_select2.forms import *


class ActivityForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = [
            'description_Activity',
            "date",
            'start_time',
            'end_time',
            'description_time',
            'employees',
            'trucks',
        ]

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['employees'].queryset = models.Employee.objects.all().order_by('first_name')
        self.fields['trucks'].queryset = models.Truck.objects.all().order_by('code')

    def clean(self):
        data = self.cleaned_data
        try:
            start_time = data['start_time']
            end_time = data['end_time']

        except:
            raise ValidationError('The start time and the end time must have the following format HH:MM')
        if start_time > end_time:
            raise ValidationError('The start time must be less than the end time')

class VistaFormAdmin(forms.ModelForm):
    class Meta:
        model = models.Vista
        fields = ['name']
