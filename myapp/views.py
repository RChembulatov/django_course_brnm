from django.shortcuts import render
from myapp.models import Product


def home(request):
    return render(request, 'home.html')


def product_list(request):
    product = Product.objects.all()
    context = dict(products=product)

    return render(request, 'product_list.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = dict(product=product)

    return render(request, 'product_detail.html', context)
