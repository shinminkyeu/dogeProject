from django.shortcuts import render
from django.db import models
from django.utils import timezone

# Create your views here.
class SolDog(models.Model):
    birth = models.IntegerField()
    breed = models.IntegerField()
    gender = models.BooleanField()
    alive = models.BooleanField(default=True)