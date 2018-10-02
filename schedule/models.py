from django.contrib.auth.models import User, Group
from django.db import models


class Vista(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return 'Cofigurations {}'.format(self.name)

    def __str__(self):
        return 'Cofigurations {}'.format(self.name)

    class Meta:
        verbose_name = 'Configuration One'
        verbose_name_plural = 'Configurations Ones'
        # Create your models here.


class Activity(models.Model):
    vista = models.ForeignKey(Vista, on_delete=models.CASCADE, null=True, blank=True)
    description_Activity = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True, help_text='The format is HH:MM')
    employees = models.ManyToManyField('Employee', related_name='activities', null=True, blank=True)
    trucks = models.ManyToManyField('Truck', related_name='activities', null=True, blank=True)

    def __str__(self):
        return self.description_Activity

    def trucks_(self):
        trucks = self.trucks.all()
        return ", ".join([truck.__str__() for truck in trucks])

    def employees_(self):
        employees = self.employees.all()
        return ", ".join([employee.__str__() for employee in employees])

    def time(self):
        return "{0}".format(self.start_time)


class Employee(User):
    can_change_password = models.BooleanField(default=False, blank=True)
    identification = models.CharField(max_length=45)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Truck(models.Model):
    code = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.code)


class Configuration(models.Model):
    employees_filter_one = models.IntegerField(choices=((1, 'Horizontal filter one'), (2, 'Tags filter one')))
    activity_filter_one = models.IntegerField(choices=((1, 'Horizontal filter one'), (2, 'Tags filter one')))
    employees_filter_two = models.IntegerField(choices=((1, 'Horizontal filter two'), (2, 'Tags filter two')))
    activity_filter_two = models.IntegerField(choices=((1, 'Horizontal filter two'), (2, 'Tags filter  two')))
    profile = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Cofigurations {}'.format(self.pk)

    def __str__(self):
        return 'Cofigurations {}'.format(self.pk)

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'


class Activity2(Activity):
    class Meta:
        verbose_name = 'Activity two'
        verbose_name_plural = 'Activitys two'
