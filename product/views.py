from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product,Category
from django.shortcuts import get_object_or_404
# Create your views here.
def landing(request):
    return render(request, "product/landing.html")


def all_products(request):
    return render(request, "product/products.html")

class ProductDetails(DetailView):
    model = Product
    template_name = 'product/detail.html'

class ListOfProduct(ListView):
    model = Product
    template_name = 'product/list.html'





