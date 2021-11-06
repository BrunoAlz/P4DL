from django.contrib import admin
from .models import Brand, Genre, Group, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProdutctsName', 'ProductPrice', 'CurrentStock', 'MinimumStock', 'DueDate', 'FkGenre', 'FkGroup', 'FkBrand',)
    search_fields = ('ProdutctsName', 'FkGenre', 'FkGroup', 'FkBrand',)
    list_filter = ('FkGenre',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'GenreName',)
    search_fields = ('GenreName',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'GroupName',)
    search_fields = ('GroupName',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'BrandName',)
    search_fields = ('BrandName',)
