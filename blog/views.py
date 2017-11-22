from django.shortcuts import render

from .models import Blog
from django.shortcuts import render


def all_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


def single_blog(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    return render(request, 'single.html', { 'blog': blog })