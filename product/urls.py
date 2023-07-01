from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import ProductViewSet

router_product = routers.DefaultRouter()
router_product.register(r'product', ProductViewSet),

urlpatterns = [
    url('/', include(router_product.urls)),
]
