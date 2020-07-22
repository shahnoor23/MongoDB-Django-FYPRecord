from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.


class Final_Year_Projects(models.Model):
    BatchYear = models.CharField(max_length=500, blank=True)
    Project_Name = models.CharField(max_length=500, blank=True)
    Project_Supervisor = models.CharField(max_length=500, blank=True)
    External_Supervisor = models.CharField(max_length=500, blank=True)
    Co_Supervisor = models.CharField(max_length=500, blank=True)
    Project_Id = models.CharField(max_length=500)
    Students = TaggableManager(blank=True)
    owner = models.ForeignKey(
        User, related_name="records", on_delete=models.CASCADE, null=True)
