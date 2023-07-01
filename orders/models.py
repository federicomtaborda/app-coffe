import datetime

from django.db import models

from client.models import Client
from product.models import Product


class Delivery(models.Model):
    name_delivery = models.CharField(max_length=150, unique=True)
    type = models.CharField(max_length=150, default='')
    active = models.BooleanField(default=True)


class Orders(models.Model):
    order_number = models.CharField(max_length=8, default='')
    product = models.ForeignKey(Product, models.DO_NOTHING)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    date = models.DateField(default=datetime.date.today)
    delibery = models.ForeignKey('Delivery', models.DO_NOTHING, blank=True, null=True)


