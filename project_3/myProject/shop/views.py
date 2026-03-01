from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, World! i am in shop app")

def product_list(request):
    # This is where you would typically fetch products from the database
    return HttpResponse('shop/product_list')