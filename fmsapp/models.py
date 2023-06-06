from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User (AbstractUser):
    image = models.ImageField(blank=True)

class Department (models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=700, default='Description goes here')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("fms:dept_single", kwargs={"pk": self.pk})
####################################################################

class DepStock (models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=700)
    count = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("fms:deptstock_single", kwargs={"pk": self.pk})

class Livestock (models.Model):
    department = models.ForeignKey(DepStock, on_delete=models.SET_NULL, null=True)
    quantity = models.CharField(blank=True, max_length=1000)
    sell = models.CharField(blank=True, max_length=10000000000)
    expense = models.CharField(blank=True, max_length=10000000000)
    date = models.CharField(max_length = 10, blank=False)
    time = models.CharField(max_length = 10, blank=False)
    

    def __str__(self):
        return self.department

    def get_absolute_url(self):
        return reverse("fms:livestock_single", kwargs={"pk": self.pk})
    
######################################################################


class FarmStock (models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=700)
    landarea = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("fms:farmstock_single", kwargs={"pk": self.pk})

class LiveFarmStock (models.Model):
    farmdepartment = models.ForeignKey(FarmStock, on_delete=models.SET_NULL, null=True)
    crop = models.CharField(blank=True, max_length=1000)
    quantity = models.CharField(blank=True, max_length=1000)
    sell = models.IntegerField()
    expense = models.IntegerField()
    harvestdate = models.CharField(max_length = 10, blank=False)
    sellingdate = models.CharField(max_length = 10, blank=False)
    time = models.CharField(max_length = 10, blank=False)

    def __str__(self):
        return self.farmdepartment+'-'+self.sellingdate

    def get_absolute_url(self):
        return reverse("fms:livefarmstock_single", kwargs={"pk": self.pk})
    

######################################################################
