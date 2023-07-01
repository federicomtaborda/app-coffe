from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import OrdersViewSet

router_orders = routers.DefaultRouter()
router_orders.register(r'orders', OrdersViewSet),

urlpatterns = [
    url('/', include(router_orders.urls)),
]
