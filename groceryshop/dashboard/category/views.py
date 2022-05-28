from django.views.generic import CreateView,UpdateView
from product.models import Category

class CreatCategory (CreateView):
    model = Category
    template_name = 'dashboard/category/create.html'
    fields = ["name", "description", 'bachground_image']


class UpdateCategory (UpdateView):
    model = Category
    template_name = 'dashboard/category/create.html'
    fields = ["name", "description", 'bachground_image']