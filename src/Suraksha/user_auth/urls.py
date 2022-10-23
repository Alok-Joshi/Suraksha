#from django.contrib import admin
#from django.urls import path,include
#from main import views
#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('', views.home, name='home')
#]

from django.urls import path
from . import views

app_name = "auth"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login")
]
