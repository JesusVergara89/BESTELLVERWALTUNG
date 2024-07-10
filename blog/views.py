from django.shortcuts import render
from blog.models import Post, Categories

# Create your views here.

def blog(request):
    post_=Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': post_})

def categories(request, categories_id):
    categ_=Categories.objects.get(id=categories_id)
    post_=Post.objects.filter(categories=categ_)
    return render(request, 'blog/categories_blog.html', {'categories': categ_, 'posts': post_})
