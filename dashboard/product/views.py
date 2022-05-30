from django.views.generic import CreateView, UpdateView, ListView
from product.models import Product
from django.utils.text import slugify


class CreateProduct(CreateView):
    model = Product
    template_name = "./dashboard/product/create.html"
    fields = ['name', 'image']

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateProduct, self).form_valid(form)


class UpdateProduct(UpdateView):
    model = Product
    template_name = "./dashboard/product/create.html"
    fields = ['name', 'description', 'price', 'weight', 'sku', 'stock', 'brand', 'category']

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateProduct, self).form_valid(form)


class ListProduct(ListView):
    model = Product
    template_name = "./dashboard/product/list.html"
    fields = ['name', 'image']
