from django.urls import path
from . import views

app_name='brand_dashboard'

urlpatterns =[
    path('create/', views.CreateBrand.as_view(), name = 'craete_brand'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name = 'update_brand'),
    path('list/', views.ListBrand.as_view(), name = 'list_brand'),
]