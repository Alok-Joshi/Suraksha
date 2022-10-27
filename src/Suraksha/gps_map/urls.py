from django.urls import path, include
from . import views
app_name = "map"

urlpatterns = [
    path('',views.get_map,name = "get_map")
    ]
