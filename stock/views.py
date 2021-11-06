from django.shortcuts import render

from utils.constants import MOVIMENT
from .models import Stock

def stock_entry(request):
    template_name = 'stock/stock_entry.html'
    objects = Stock.objects.filter(MovementStatus='E')
    context = {
        'stock': objects
    }
    return render(request, template_name, context)


def stock_entry_detail(request, pk):
    template_name = 'stock/stock_entry_detail.html'
    obj = Stock.objects.get(pk=pk)
    context = {
        'stockDetail': obj
    }
    return render(request, template_name, context)
