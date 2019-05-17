from django.shortcuts import render
from django.db import models
from django.utils import timezone

# Create your views here.
class DogInput(models.Model):
    birth = models.DateField()
    breed = models.IntegerField()
    gender = models.BooleanField()
    alive = models.BooleanField(default=True)