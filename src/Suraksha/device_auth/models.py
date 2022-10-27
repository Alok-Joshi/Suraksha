from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Device(models.Model):
    device_uid = models.CharField(max_length=20, primary_key=True, null=False)
    #additional meta data related to a device can be added here. This is admin relevant meta data of the device

class owns(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    device = models.OneToOneField(Device, on_delete=models.PROTECT)
    device_name = models.CharField(max_length=20,default="userdevice")
    #device_name is user specific metadata of the device. This metadata cna be later put into a different tabled and foreign keyed here
    
