from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
        re_path(r'ws/coordinates/(?<device_name>\w+)/$',consumers.gps_coordinates.as_asgi())
        ]
