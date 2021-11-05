from django.shortcuts import render
from .models import Product

def list_product(request):
    template_name = 'list_product.html'
    objects = Product.objects.all()
    context = {
        'object_list': objects
    }
    return render(request, template_name, context)
