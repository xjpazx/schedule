from django.urls import path
from schedule import views

app_name = 'schedule'

urlpatterns = [
    path('ws/schedule/', views.ScheduleView.as_view(), name='ws_schedule'),
]