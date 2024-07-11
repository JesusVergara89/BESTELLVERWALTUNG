from django.shortcuts import render, get_object_or_404
from store.models import Product, Store_category

# Create your views here.
def store(request):
    products_=Product.objects.all()
    products_ids_queryset = Product.objects.values_list('category_id', flat=True)
    product_ids = list(products_ids_queryset)
    seen = set()
    product_ids_unique = []
    for prodt in product_ids:
         if prodt not in seen:
             product_ids_unique.append(prodt)
             seen.add(prodt)
    categ_=Store_category.objects.filter(id__in=product_ids_unique)
    return render(request, 'store/store.html', {'products': products_, 'categories': categ_})

def categories_products(request, _id):
    categ_=Store_category.objects.get(id=_id)
    product_=Product.objects.filter(category_id = categ_)
    return render(request, 'store/categories_post.html', {'products': product_})
