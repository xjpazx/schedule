from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics

from .Serializer import ActivitySerializer
from .models import Activity


class ActivityList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
