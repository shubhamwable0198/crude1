from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    salary = models.IntegerField()
    city = models.CharField(max_length=40)
    dob = models.DateField()