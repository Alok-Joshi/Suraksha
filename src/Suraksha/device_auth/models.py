from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Device(models.Model):
    device_uid = models.CharField(max_length=20, primary_key=True, null=False)
    device_name = models.CharField(max_length=20)

class owns(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    device = models.OneToOneField(Device, on_delete=models.PROTECT)
    
