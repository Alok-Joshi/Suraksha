from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200, null=False,help_text = None)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
# Create your models here.
