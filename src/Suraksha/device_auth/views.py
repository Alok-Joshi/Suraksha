from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import OwnershipForm
from .models import Device, owns
import logging

def device_used(device_uid):
    """Checks if a given give is already used """
    result_set = owns.objects.get(device_uid = device_uid)
    return result_set.exists()
    
@login_required
def own_device(request):
        if request.method == 'GET':
            form = OwnershipForm()
            return render(request, 'device_auth/own_device.html', {'form': form, 'errors':[]})

        else:
            form = OwnershipForm(request.POST)
            if(form.is_valid()):

                device_uid = form.__getitem__('device_mac').value()
                device_name = form.__getitem__('device_name').value()

                try:
                    if not device_used(device_uid):
                        device = Device.objects.get(device_uid = device_uid)
                        ownership_obj = owns.objects.create(user=request.user, device=device)
                        ownership_obj.save()

                        return HttpResponse("<h1>Device Ownership changed sucessfully!</h1>")
                    else:
                        return render(request, 'device_auth/own_device.html', {'form': OwnershipForm(), 'errors':['Entered device is already in use']})
                except Exception as e:
                    logging.error(e)
                    return render(request, 'device_auth/own_device.html', {'form': OwnershipForm(), 'errors':['Entered device not found']})              
            return render(request, 'device_auth/own_device.html', {'form': OwnershipForm(), 'errors':["Entered data was invalid", form.errors]})

# Create your views here.
# class Authenticate(TemplateView):
#     def get(self, request):
#         form = OwnershipForm()
#         return render(request, "device_auth/auth.html", {'form':form})
    
#     def post(self, request):
#         form = OwnershipForm(request.POST)
#         if(form.is_valid()):
#             device = form.data.get('device')
#             ownership = Device.objects.get(device_uid = device)
#             if not ownership.used:
#                 ownership.used = 1
#                 form.save()
#                 return HttpResponse("<h1>Ownership successfully changed! </h1>")
#             else:
#                 return HttpResponse("<h1>Already Owned</h1>")
#         return render(request, "device_auth/auth.html", {'form':form})
