from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.get_map,name = "get_map")
    ]
