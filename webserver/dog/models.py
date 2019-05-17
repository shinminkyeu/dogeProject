import datetime
import re

from django.db import models
from django.utils import timezone

# Create your models here.
class Dog(models.Model):
    dog_id = models.IntegerField()
    
class Picture(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    picture_url = models.CharField(max_length=200)
