from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import DeviceForm, OwnershipForm
from .models import Device, owns


@login_required
def add_device(request):
        if request.method == 'GET':
            form = DeviceForm()
            return render(request, 'device_auth/add_device.html', {'form': form})
        else:
            breakpoint()
            form = DeviceForm(request.POST)
            if(form.is_valid()):
                form.save()
                return HttpResponse("<h1>Sucessfully device added</h1>")
            return render(request, 'device_auth/add_device.html', {'form': form})
# Create your views here.
class Authenticate(TemplateView):
    def get(self, request):
        form = OwnershipForm()
        return render(request, "device_auth/auth.html", {'form':form})
    
    def post(self, request):
        form = OwnershipForm(request.POST)
        if(form.is_valid()):
            device = form.data.get('device')
            ownership = Device.objects.get(device_uid = device)
            if not ownership.used:
                ownership.used = 1
                form.save()
                return HttpResponse("<h1>Ownership successfully changed! </h1>")
            else:
                return HttpResponse("<h1>Already Owned</h1>")
        return render(request, "device_auth/auth.html", {'form':form})

