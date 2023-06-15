from django.db import models

# Create your models here.


class CustomCustomer(models.Model):
    name = models.CharField(max_length=200, blank=True)
    dob = models.DateField(blank=True, null=True)
    father_name = models.CharField(max_length=200, blank=True, null=True)
    mother_name = models.CharField(max_length=200, blank=True, null=True)
    spouse_name = models.CharField(max_length=200, blank=True, null=True)
    occupation = models.CharField(max_length=200, blank=True, null=True)
    village = models.CharField(max_length=200, blank=True, null=True)
    post_office = models.CharField(max_length=200, blank=True, null=True)
    thana = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    division = models.CharField(max_length=200, blank=True, null=True)