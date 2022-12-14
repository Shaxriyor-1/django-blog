from django.shortcuts import render
from .models import Blog, Author

# Create your views here.


def index(request):
    return render(request, 'index.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs':blogs})


def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog_detail.html', {'blog': blog})
