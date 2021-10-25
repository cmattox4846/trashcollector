from django.db import models

# Create your models here.

<<<<<<< HEAD
=======
class Employee(models.Model):
    name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    badge_number = models.IntegerField()
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
>>>>>>> 1ce14df495cb91d4ffdac056dcb56b01226411b5
