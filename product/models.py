import datetime

from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=150, default='')
    active = models.BooleanField(default=True)


class Product(models.Model):
    name_product = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=150, default='')
    category = models.ForeignKey('Category', models.DO_NOTHING)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)
