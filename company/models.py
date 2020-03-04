from django.db import models


class Employee(models.Model):
    # input fields
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True, default=None)
    weight = models.FloatField(null=True, blank=True, default=None)

