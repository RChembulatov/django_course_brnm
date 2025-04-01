from django.urls import path
from .views import home, product_list

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
]
