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

    def clean(self):
        data = self.cleaned_data
        try:
            start_time = data['start_time']
            end_time = data['end_time']
            print(start_time)
            print(end_time)

        except:
            if start_time > end_time:
                raise ValidationError('The start time must be less than the end time')
            else:
                raise ValidationError('The start time and the end time must have the following format HH:MM')
        return self.cleaned_data


class VistaFormAdmin(forms.ModelForm):
    class Meta:
        model = models.Vista
        fields = ['name']
