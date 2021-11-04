from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProdutctsName', 'CurrentStock', 'MinimumStock',)
    search_fields = ('ProdutctsName',)
