from django.urls import include, path
from .views import Authenticate

app_name = 'authenticate'
urlpatterns = [
    path('authenticate/', Authenticate.as_view(), name = 'authenticate'),
]
