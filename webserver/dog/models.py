import datetime
import re

from django.db import models
from django.utils import timezone

# Create your models here.
class Dog(models.Model):
    birth = models.IntegerField()
    