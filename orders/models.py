from django.db import models


class Orders(models.Model):
    order_number = models.CharField(max_length=8, default='')
