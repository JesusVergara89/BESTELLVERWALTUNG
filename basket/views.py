from django.shortcuts import render, redirect
from .basket import basket
from store.models import Product

# Create your views here.

def add_product(request, product_id):
    _basket= basket(request)
    _product=Product.objects.get(id=product_id)
    _basket.add(product=_product)
    return redirect("store")

def product_delete(request, product_id):
    _basket= basket(request)
    _product=Product.objects.get(id=product_id)
    _basket.delete_product(product=_product)
    return redirect("store")

def product_substract(request, product_id):
    _basket= basket(request)
    _product=Product.objects.get(id=product_id)
    _basket.substract_product(product=_product)
    return redirect("store")


def basket_clean(request, product_id):
    _basket= basket(request)
    _basket.clean_basket()
    return redirect("store")