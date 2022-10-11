"""
ASGI config for Suraksha project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import data_streamer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Suraksha.settings')

application = ProtocolTypeRouter({
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    data_streamer.routing.websocket_urlpatterns
                    )
                )
            ),
        })

