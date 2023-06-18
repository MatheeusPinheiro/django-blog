from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post

# Create your views here.

def Home(request):
    
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'posts': post
    }    
    return render(request, 'blog/post_detail.html', context)
