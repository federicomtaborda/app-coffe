from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Orders
from .serializers import OrdersSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class OrdersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    pagination_class = StandardResultsSetPagination
