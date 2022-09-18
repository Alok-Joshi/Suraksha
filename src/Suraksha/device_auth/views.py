from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import DeviceForm


@csrf_protect
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
        return render(request, "device_auth/auth.html")
