from django.urls import include, path
from . import views

app_name = 'authenticate'
urlpatterns = [
    path('authenticate/', views.Authenticate.as_view(), name = 'authenticate'),
    path('add-device/', views.add_device, name='add_device'),
]
