from django.views.generic.edit import UpdateView
from .models import Product
from .forms import ProductForm
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

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


class ProductCreate(CreateView):
    model = Product
    template_name = 'product/form_product.html'
    form_class = ProductForm


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product/form_product.html'
    form_class = ProductForm