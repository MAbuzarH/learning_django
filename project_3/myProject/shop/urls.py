from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.home, name='home'),
    path('shop/products/', views.product_list, name='product_list'),
]