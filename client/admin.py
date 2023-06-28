from django.contrib import admin

# Register your models here.
from client.models import Client, Entity


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', )
    search_fields = ['id', ]


@admin.register(Entity)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('entity', 'location', )
    search_fields = ['id', ]
