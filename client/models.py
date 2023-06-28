from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=150, unique=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    entity_name = models.ForeignKey('Entity', models.DO_NOTHING, blank=True, null=True)


class Entity(models.Model):
    entity = models.CharField(max_length=150)
    address = models.CharField(max_length=70, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
