from django.urls import path,include
from .brand import urls as brand_url
from .category import urls as category_url
from .product import urls as product_url

app_name = 'dashboard'

urlpatterns = [
    path('category/', include(category_url,namespace='category_dashboard')),
    path('brand/', include(brand_url,namespace='brand_dashboard')),
    path('product/', include(product_url,namespace='product_dashboard')),

]