from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Authenticate(TemplateView):
    def get(self, request):
        return render(request, "device_auth/auth.html")
