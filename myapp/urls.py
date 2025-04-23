from django.urls import path
from .views import ContactView, contact_form_success_view, home, product_list, product_detail, ItemListView

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('item-list/', ItemListView.as_view(),
         name='item_list_with_pagination'),
    path('contact-form/', ContactView.as_view(), name='contact_form'),
    path('contact-form/success/', contact_form_success_view,
         name='contact_form_success'),
]
