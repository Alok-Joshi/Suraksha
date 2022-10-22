from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from device_auth.models import Device,owns

@login_required
def get_map(request):
    """ Renders the map. Login is required """
    if(request.method == "GET"):
            devices = owns(user = request.user)
            return render(request,"gps_map/map.html",{'devices':devices})

