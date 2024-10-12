import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from pages.routing import wsPattern

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')  # Adjust as necessary

http_response_app = get_asgi_application()

application = ProtocolTypeRouter(
    {"http": http_response_app, "websocket": URLRouter(wsPattern)}
)