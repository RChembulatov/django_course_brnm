from django.urls import path
from .views import home, product_list, product_detail, ItemListView

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('item-list/', ItemListView.as_view(),
         name='item_list_with_pagination'),
]
