from django.shortcuts import render
from blog.models import Post

# Create your views here.

def blog(request):
    post_=Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': post_})
