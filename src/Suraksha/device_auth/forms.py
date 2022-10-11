from dataclasses import field
from django import forms
from .models import Device, owns

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_uid']

class OwnershipForm(forms.ModelForm):
    class Meta:
        model = owns
        fields = ['device', 'user']