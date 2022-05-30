from django.urls import path
from . import views

app_name = 'product_dashboard'

urlpatterns = [
    path('create/', views.CreateProduct.as_view(), name='product_create'),
    path('update/<int:pk>/', views.UpdateProduct.as_view(), name='product_update'),
    path('list/', views.ListProduct.as_view(), name='product_list'),
]
