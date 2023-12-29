from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from blog.models import Post, Category

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    pick_posts = Post.objects.filter(status=Post.ACTIVE, pick_posts=True)
    
    categories = Category.objects.annotate(num_posts=Count('posts')).all()

    return render(request, 'core/home.html', {'posts': posts, 'pick_posts': pick_posts, 'categories': categories})

def about(request):
    return render(request, 'core/about.html')

def poetry(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    pick_posts = Post.objects.filter(status=Post.ACTIVE, pick_posts=True)
    
    categories = Category.objects.annotate(num_posts=Count('posts')).all()
    return render(request, 'core/poetry.html', {'posts': posts, 'pick_posts': pick_posts, 'categories': categories})

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
