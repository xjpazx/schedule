from django.contrib import admin
from easy_select2 import apply_select2
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple
from cuser.middleware import CuserMiddleware

from .models import Activity, Employee, Truck, Configuration, Vista, Activity2
from schedule import forms as forms_
from django import forms


@admin.register(Activity)
class AdminActivity(admin.ModelAdmin):
    list_display = (
        'trucks_',
        'employees_',
        'description_Activity',
        'time',

    )
    search_fields = ['description_Activity', 'description_time']
    form = forms_.ActivityForm

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        user = CuserMiddleware.get_user()
        if user.groups.all().first():
            if user.groups.all().first().configuration_set.all().first():
                configuration = user.groups.all().first().configuration_set.all().first()
                if db_field.name == 'trucks':
                    kwargs['widget'] = apply_select2(forms.SelectMultiple) if configuration.activity_filter_one == 2 else SortedFilteredSelectMultiple()
                elif 'employees' == db_field.name:
                    kwargs['widget'] = apply_select2(forms.SelectMultiple) if configuration.employees_filter_one == 2 else SortedFilteredSelectMultiple()
                return super(AdminActivity, self).formfield_for_manytomany(db_field, request, **kwargs)
            else:
                if db_field.name in ['trucks', 'employees']:
                    kwargs['widget'] = apply_select2(forms.SelectMultiple)
                return super(AdminActivity, self).formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Activity2)
class AdminActivity2(admin.ModelAdmin):
    list_display = (
        'trucks_',
        'employees_',
        'description_Activity',
        'time',

    )
    search_fields = ['description_Activity', 'description_time']
    form = forms_.ActivityForm

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        user = CuserMiddleware.get_user()
        if user.groups.all().first():
            if user.groups.all().first().configuration_set.all().first():
                configuration = user.groups.all().first().configuration_set.all().first()
                if db_field.name == 'trucks':
                    kwargs['widget'] = apply_select2(forms.SelectMultiple) if configuration.activity_filter_two == 2 else SortedFilteredSelectMultiple()
                elif 'employees' == db_field.name:
                    kwargs['widget'] = apply_select2(forms.SelectMultiple) if configuration.employees_filter_two == 2 else SortedFilteredSelectMultiple()
                return super(AdminActivity2, self).formfield_for_manytomany(db_field, request, **kwargs)
            else:
                if db_field.name in ['trucks', 'employees']:
                    kwargs['widget'] = apply_select2(forms.SelectMultiple)
                return super(AdminActivity2, self).formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = (
        'identification',
        'first_name',
        'last_name',
        'can_change_password',
    )

    def save_model(self, request, obj, form, change):
        password = obj.password
        obj.set_password(password)
        super().save_model(request, obj, form, change)


@admin.register(Truck)
class AdminTruck(admin.ModelAdmin):
    list_display = (
        'code',
    )

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['activity_filter_one', 'employees_filter_one', 'profile']



