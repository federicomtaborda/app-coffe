from django.contrib import admin

# Register your models here.
from orders.models import Orders, Delivery


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_number',)
    search_fields = ['id', ]


@admin.register(Delivery)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name_delivery',)
    search_fields = ['id', ]
