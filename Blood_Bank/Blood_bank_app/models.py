from django.db import models

# Create your models here.
class DonorDetails(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=20)
    age = models.BigIntegerField()
    phone_number = models.BigIntegerField()
