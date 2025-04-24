from django.shortcuts import render
from django.urls import reverse_lazy
from myapp.forms import ContactForm, ReviewForm
from myapp.models import Product, Item
from django.views.generic import ListView
from django.views.generic.edit import FormView, FormMixin


def home(request):
    return render(request, 'home.html')


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = dict(product=product)

    return render(request, 'product_detail.html', context)


class ItemListView(ListView):
    model = Item
    template_name = 'item_list_with_pagination.html'
    context_object_name = 'item_list'
    paginate_by = 5


def form_success_view(request):
    return render(request, 'form_success.html')


class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('form_success')

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)


class ProductListView(FormMixin, ListView):
    model = Product
    form_class = ReviewForm
    template_name = 'product_list.html'
    paginate_by = 2
    context_object_name = 'products'
    success_url = reverse_lazy('form_success')

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
