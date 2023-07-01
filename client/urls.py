from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import ClientViewSet, EntityViewSet

router_client = routers.DefaultRouter()
router_client.register(r'client', ClientViewSet),
router_client.register(r'entity', EntityViewSet),


urlpatterns = [
    url('/orders', include(router_client.urls)),
]
