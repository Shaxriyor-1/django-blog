from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import BlogForm
from .models import Blog, Profile

# Create your views here.


def index(request):
    return render(request, 'index.html')


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs':blogs})


def search(request):
    query = request.GET.get("search")
    blogs = Blog.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


def blog_create(request):
    form = BlogForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("main:blog_list")
    return render(request, 'post_create.html', {"form": form})
