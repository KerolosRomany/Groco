from django.views.generic import CreateView, UpdateView
from product.models import product
from django.utils.text import slugify


class CreateProduct(CreateView):
    model = product
    template_name = "./product/create.html"
    fields = ['name', 'image']

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(CreateProduct, self).form_valid(form)


class UpdateProduct(UpdateView):
    model = product
    template_name = "./product/create.html"
    fields = ['name', 'description', 'price', 'weight', 'sku', 'stock', 'brand', 'category']

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        return super(UpdateProduct, self).form_valid(form)


class ListProduct(UpdateView):
    model = product
    template_name = "./brand/list.html"
    fields = ['name', 'image']
