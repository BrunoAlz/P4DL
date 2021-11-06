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

def __str__(self):
    return self.MovementStatus