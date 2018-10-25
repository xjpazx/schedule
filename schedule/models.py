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


class Area(models.Model):
    id_Area=models.CharField(max_length=200,null=True,blank=True)
    name_Area=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name_Area


class Activity(models.Model):
    area_fk=models.ForeignKey(Area, blank=True, null=True, on_delete=models.CASCADE)
    STATE = (
        (1, 'To start'),
        (2, 'In progress'),
        (3, 'Done')
    )
    vista = models.ForeignKey(Vista, on_delete=models.CASCADE, null=True, blank=True)
    description_Activity = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True, help_text='The format is HH:MM')
    end_time = models.TimeField(blank=True, null=True, help_text='The format is HH:MM')
    state=models.IntegerField(max_length=20,choices=STATE,default='To Start')

    def __str__(self):
        return self.description_Activity

    def time(self):
        return "{0}".format(self.start_time)


class Employee(User):
    area_fk=models.ForeignKey(Area, null=True, on_delete=models.CASCADE)
    STATE = (
        ('AVAILABLE', 'AVAILABLE'),
        ('NOT AVAILABLE', 'NOT AVAILABLE'),
        ('NC/NS', 'NC/NS'),
        ('SICK', 'SICK'),
        ('OFF', 'OFF')
    )
    identification = models.CharField(max_length=45)
    state=models.CharField(max_length=200,choices=STATE,default='AVAILABLE')
    user_With_Permissions=models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Truck(models.Model):
    code = models.CharField(max_length=100)
    state = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.code)


class Assignment(models.Model):
    STATE = (
        (1, 'To start'),
        (2, 'In progress'),
        (3, 'Done')
    )
    activity_fk = models.ForeignKey(Activity, null=True, on_delete=models.CASCADE)
    employees = models.ManyToManyField('Employee', related_name='activities', blank=True)
    trucks = models.ManyToManyField('Truck', related_name='activities', blank=True)
    state = models.IntegerField(max_length=20, choices=STATE, default='To Start')

    def __str__(self):
        return '{}'.format(self.code)

    def trucks_(self):
        trucks = self.trucks.all()
        return ", ".join([truck.__str__() for truck in trucks])

    def employees_(self):
        employees = self.employees.all()
        return ", ".join([employee.__str__() for employee in employees])