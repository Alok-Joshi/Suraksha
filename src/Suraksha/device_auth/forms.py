from dataclasses import field
from django import forms
from .models import Device, owns

class AddDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_uid']

class OwnershipForm(forms.Form):
    device_mac = forms.CharField(max_length=20, label="Device UID")
    user = forms.CharField(max_length=200, label="Username")