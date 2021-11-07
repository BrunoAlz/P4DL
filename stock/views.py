from django.forms.models import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, resolve_url

from .forms import StockForm, StockItemsForm

from .models import Stock, StockItems


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


def stock_entry_add(request):
    template_name = 'stock/stock_entry_form.html'
    stock_form = Stock()
    stock_item_formset = inlineformset_factory(
        Stock,
        StockItems,
        form=StockItemsForm,
        extra=0,
        min_num=1,
        validate_min=True
    )
    if request.method == 'POST':
        form = StockForm(
            request.POST,
            instance=stock_form,
            prefix='main')
        formset = stock_item_formset(
            request.POST,
            instance=stock_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            url = 'stock:stock_entry_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = StockForm(instance=stock_form, prefix='main')
        formset = stock_item_formset(instance=stock_form, prefix='estoque')

    context = {
        'form': form,
        'formset': formset
    }
    return render(request, template_name, context)
