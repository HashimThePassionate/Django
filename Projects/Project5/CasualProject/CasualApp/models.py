from django.db import models
# Create your models here.
class Time(models.Model):
    day = models.CharField(max_length=50, unique=True)
    opening_hours = models.CharField(max_length=100)
