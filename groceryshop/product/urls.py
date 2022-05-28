from django.urls import path

from groceryshop.product import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('products/', views.all_products, name="all_products"),
]
