import datetime
import re

from django.db import models

# Create your models here.
class Dog(models.Model):
    dog_id = models.IntegerField(primary_key=True)
    dog_coat_length = models.PositiveSmallIntegerField(null=True, blank=True)
    dog_coat_color = models.CharField(max_length=100, null=True, blank=True)

class Picture(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    picture_url = models.ImageField(upload_to=dog)

class Breed(models.Model):
    breed_kind = models.CharField(max_length=100)
    breed_size = models.PositiveSmallIntegerField()