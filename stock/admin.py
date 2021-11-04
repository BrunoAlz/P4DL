from django.contrib import admin
from django.db import models
from .models import Stock, StockItems


class StockItemsInline(admin.TabularInline):
    model = StockItems
    extra = 0

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = (StockItemsInline,)
    list_display = ('ResponsibleUser', 'MovementStatus', 'CreationDate',)
    search_fields = ('ResponsibleUser',)
    list_filter = ('MovementStatus',)
    date_hierarchy = 'CreationDate'