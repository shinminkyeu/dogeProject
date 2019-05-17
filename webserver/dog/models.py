import datetime
import re

from django.db import models

# Create your models here.
class Dog(models.Model):
    dog_id = models.IntegerField(primary_key=True)
    dog_picture_counter = models.PositiveIntegerField(default = 0)
    dog_coat_length = models.PositiveSmallIntegerField(null=True, blank=True)
    dog_coat_color = models.CharField(max_length=100, null=True, blank=True)

def pic_name_policy(instance, filename):
    instance.dog.dog_picture_counter += 1
    return '%s/%s.%s' % (
        instance.dog.dog_id,
        instance.dog.dog_picture_counter,
        filename.split('.')[-1]
        )

class Picture(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    picture_url = models.ImageField(upload_to=pic_name_policy)

class Breed(models.Model):
    breed_kind = models.CharField(max_length=100)
    breed_size = models.PositiveSmallIntegerField()