from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from schedule.forms import ActivityForm
import json


class ScheduleView(View):
    def post(self, request, *args, **kwargs):
        form = ActivityForm(request.POST)
        if form.is_valid():
            addform = form.save(commit=False)
            addform.save()
            return HttpResponse('{}', content_type='application/json')
        response = form.errors.as_json()

        return HttpResponse(response, content_type='application/json')