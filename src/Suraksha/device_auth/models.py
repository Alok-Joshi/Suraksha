from django.db import models
from login.models import User

# Create your models here.
class Device(models.Model):
    device_uid = models.CharField(max_length=20, primary_key=True, null=False)
    used = models.BooleanField(default=0)

class owns(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
