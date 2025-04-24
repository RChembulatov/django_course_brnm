from django.urls import path
from .views import ContactView, ProductListView, form_success_view, home, product_detail, ItemListView

urlpatterns = [
    path('', home, name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('item-list/', ItemListView.as_view(),
         name='item_list_with_pagination'),
    path('contact-form/', ContactView.as_view(), name='contact_form'),
    path('form-success/', form_success_view, name='form_success'),
]
