from django.shortcuts import render


# Create your views here.
def landing(request):
    return render(request, "product/landing.html")


def all_products(request):
    return render(request, "product/products.html")