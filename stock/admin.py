from django.contrib import admin
from django.db import models
from .models import Stock, StockItems


class StockItemsInline(admin.TabularInline):
    """
    Criaremos uma uma linha com os dados da Model StockItems,
    o atributo extra = 0 é o número de linhas que podemos adicionar por vez,
    podemos colocar várias linhas que serão exibidas conforme a quantidade que
    escolhermos
    """
    model = StockItems
    extra = 0

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    """
    Chamamos a classe StockItemsInline dentro de inlines e passamos os outros
    atributos para melhorar a interação com o django admin
    """
    inlines = (StockItemsInline,)
    list_display = ('ResponsibleUser', 'MovementStatus', 'CreationDate',)
    search_fields = ('ResponsibleUser',)
    list_filter = ('MovementStatus',)
    date_hierarchy = 'CreationDate'