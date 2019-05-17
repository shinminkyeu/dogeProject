from django.db import models

# Create your models here.
class User(models.Model):
    user_address = models.CharField(max_length=42, primary_key=True)
    user_name = models.CharField(max_length=10)
    user_contact = models.CharField(max_length=15)