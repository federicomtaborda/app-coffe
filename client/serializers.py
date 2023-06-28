from rest_framework import serializers
from client.models import Client, Entity


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    entity_name = EntitySerializer(many=False, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
