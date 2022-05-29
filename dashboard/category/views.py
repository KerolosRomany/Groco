from django.utils.text import slugify
from django.shortcuts import get_object_or_404,render
from django.template.response import TemplateResponse
from django.views.generic import CreateView,UpdateView,ListView
from product.models import Category
# Create your views here.


class CreateCategory(CreateView):
    model = Category
    template_name = './category/create.html'
    fields = ["name","descriptions","background_image"]

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name)+"-"+str(instance.id)
        instance.save()
        return super(CreateCategory,self).form_valid(form)

class CreateSubCategory(CreateView):
    model = Category
    template_name = './category/create.html'
    fields = ["name","descriptions","background_image"]

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name)+"-"+str(instance.id)
        instance.parent = Category.objects.get(id=int(self.kwargs.get('pk')))
        instance.save()
        return super(CreateSubCategory,self).form_valid(form)

class UpdateCategory(UpdateView):
    model = Category
    template_name = './product/landing.html'
    fields = ["name","descriptions","background_image"]
    def form_valid(self,form):
        instance = form.instance
        instance.slug = slugify(instance.name)+"-"+str(instance.id)
        instance.save()
        return super(UpdateCategory,self).form_valid(form)

class CategoryList(ListView):
    model = Category
    template_name = "./category/list.html"


def category_detail(request,pk):
    root= get_object_or_404(Category,pk=pk)
    path= root.get_ancestores(iclude_self=True)
    categories= root.get_children().order_by('name')
    context={
        'root':root,
        'path':path,
        'categories':categories
    }
    return  render(request, './category/detail.html', context)



