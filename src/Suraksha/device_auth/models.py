from django.db import models
from login.models import User

# Create your models here.
class Device(models.Model):
    device_uid = models.CharField(max_length=20, primary_key=True, null=False)
    used = models.BooleanField(default=0)

class owns(models.Model):
    user = models.CharField(max_length=200, null=False)
    device = models.CharField(max_length=200, null=False)
