from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from device_auth.models import Device,owns
import pdb

@login_required
def get_map(request):
    """ Renders the map. Login is required """
    if(request.method == "GET"):
            result_set = owns.objects.filter(user = request.user)
            return render(request,"gps_map/map.html",{'result_set':result_set})

