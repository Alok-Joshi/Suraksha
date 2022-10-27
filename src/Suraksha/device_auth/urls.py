from django.urls import include, path
from . import views

app_name = 'device_auth'
urlpatterns = [
    # path('authenticate/', views.Authenticate.as_view(), name = 'authenticate'),
    path('own-device/', views.own_device, name='own_device'),
]
