from django.contrib import admin
from easy_select2 import apply_select2
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple
from cuser.middleware import CuserMiddleware

from .models import Activity, Employee, Truck,Assignment, Vista, Area
from schedule import forms as forms_
from schedule import forms


class AssignmentInline(admin.StackedInline):
    model = Assignment
    extra = 0


@admin.register(Activity)
class AdminActivity(admin.ModelAdmin):

    list_display = (
        'area_fk',
        'start_date',
        'end_date',
        'description_Activity',
        'start_time',
        'end_time',
        'state',
    )
    list_display_links = ('description_Activity',)
    search_fields = ['description_Activity']
    form = forms.ActivityForm
    inlines = [AssignmentInline]

    def get_queryset(self, request):
        query = super(AdminActivity, self).get_queryset(request)
        return query.order_by('start_date__year', 'start_date__month', '-start_date__day')

@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = (
        'area_fk',
        'identification',
        'first_name',
        'last_name',
        'state',
        'user_With_Permissions',
    )


@admin.register(Truck)
class AdminTruck(admin.ModelAdmin):
    list_display = (
        'code',
        'state',
    )


@admin.register(Area)
class AdminArea(admin.ModelAdmin):
    list_display = (
        'id_Area',
        'name_Area',
    )


@admin.register(Assignment)
class AdminAssignment(admin.ModelAdmin):
    list_display = (
        'activity_fk',
        'employees_',
        'trucks_',
        'state',
    )
    form = forms.AssignmentForm

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        kwargs['widget'] = SortedFilteredSelectMultiple()
        return super(AdminAssignment, self).formfield_for_manytomany(db_field, request, **kwargs)


