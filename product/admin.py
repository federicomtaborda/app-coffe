from django.contrib import admin

# Register your models here.
from product.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product',)
    search_fields = ['id', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category',)
    search_fields = ['id', ]
