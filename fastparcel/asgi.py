import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from fastparcel.urls import websocket_urlpatterns


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fastparcel.settings")
# django_asgi_app = get_asgi_application()




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fastparcel.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
      URLRouter(websocket_urlpatterns)
    )
})