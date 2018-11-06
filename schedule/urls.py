from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from schedule import views
from schedule.views import AssignmentView, AreaView, ActivityView, EmployeeView, TruckView

routes = DefaultRouter()
app_name = 'schedule'
routes.register('assignments', AssignmentView)
routes.register('areas', AreaView)
routes.register('activitys', ActivityView)
routes.register('employees', EmployeeView)
routes.register('trucks', TruckView)

urlpatterns = [
    path('ws/schedule/', views.ScheduleView.as_view(), name='ws_schedule'),
    path('', include(routes.urls)),
]