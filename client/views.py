from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Client, Entity
from .serializers import ClientSerializer, EntitySerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = StandardResultsSetPagination


class EntityViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

