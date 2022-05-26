from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import CreateView,UpdateView,ListView
from product.models import Category
# Create your views here.



class CreateCategory(CreateView):
    model = Category
    template_name = 'product\landing.html'
    fields = ["name","descriptions","background_image"]

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name)+"-"+str(instance.id)
        instance.save()
        return super(CreateCategory,self).form_valid(form)

class UpdateCategory(UpdateView):
    model = Category
    template_name = 'product\landing.html'
    fields = ["name","descriptions","background_image"]

class CategoryList(ListView):
    model = Category
    template_name = "product\products.html"
    def form_valid(self,form):
        instance = form.save()
        instance.slug = slugify(instance.name)+"-"+str(instance.id)
        instance.save()
        return super(CreateCategory,self).form_valid(form)


