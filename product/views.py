from django.shortcuts import render
from .models import Product

def list_product(request):
    template_name = 'product/list_product.html'
    objects = Product.objects.all()
    context = {
        'object_list': objects
    }
    return render(request, template_name, context)


def detail_product(request, pk):
    template_name = 'product/detail_product.html'
    details = Product.objects.get(pk=pk)
    context = {
        'detail': details
    }
    return render(request, template_name, context)


def add_product(request):
    template_name = 'product/form_product.html'
    return render(request, template_name)