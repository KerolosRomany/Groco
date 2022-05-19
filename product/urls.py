from django.urls import path

from product import views

urlpatterns = [
    path('', views.landing, name="landing")
]
