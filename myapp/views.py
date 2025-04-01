from django.shortcuts import render
from myapp.models import Product


def home(request):
    return render(request, 'home.html')


def product_list(request):
    product = Product.objects.all()
    context = dict(products=product)

    return render(request, 'product_list.html', context)
