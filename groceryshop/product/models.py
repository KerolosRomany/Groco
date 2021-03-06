from email.mime import image
from itertools import product
from django.urls import reverse,reverse_lazy
from unicodedata import name
from django.db import models
from mptt.models import MPTTModel
from mptt.managers import TreeManager

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    description = models.TextField()
    background_image = models.ImageField(upload_to='categor background',blank=True)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    tree = TreeManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy()

class Brand(models.Model):
    name = models.CharField(max_length=225) 
    slug = models.SlugField(max_length=225)
    image = models.ImageField() 

class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.FloatField()
    weight = models.FloatField()
    sku = models.CharField(max_length=30,unique=True)
    stock = models.PositiveBigIntegerField()
    brand = models.ForeignKey('Brand',on_delete=models.CASCADE)
    rate =models.Avg()
    def __str__(self):
        return self.name




class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    alt = models.CharField(max_length=225)


