from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Blog


def all_blog(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 2)  # 3 блог нэг хуудсанд харуулна.
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'blogs': blogs})


def single_blog(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    return render(request, 'single.html', { 'blog': blog })
