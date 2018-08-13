from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Blog


def all_blog(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)  # хуудсанд 3 блог харуулна

    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'index.html', {'blogs': blogs})


def single_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'single.html', {'blog': blog})
