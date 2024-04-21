"""
ASGI config for main project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django 
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import leads.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http" : django_asgi_app,
    "websocket" : AuthMiddlewareStack(
        URLRouter(
            leads.routing.websocket_urlpatterns
        )
    )
    
})