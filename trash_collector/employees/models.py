from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    