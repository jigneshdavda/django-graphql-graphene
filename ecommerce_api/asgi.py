import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer
# from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # "http": django_asgi_app,
    "websocket": URLRouter([
        path('graphql/', GraphqlSubscriptionConsumer)
    ]),
})