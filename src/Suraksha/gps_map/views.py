from django.shortcuts import render


def get_map(request):
    """ Renders the map. Login is required """
    return render(request,"gps_map/map.html")
    if(request.user.is_authenticated):
        #get the devices linked to user, pass them as context to template, render template
        pass

    else:
        #redirect to the login page 
        pass
