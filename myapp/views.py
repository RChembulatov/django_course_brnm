from django.shortcuts import render
from myapp.models import Product, Item
from django.views.generic import ListView


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


class ItemListView(ListView):
    model = Item
    template_name = 'item_list_with_pagination.html'
    context_object_name = 'item_list'
    paginate_by = 5
