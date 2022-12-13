from django.shortcuts import render
from .models import Blog

# Create your views here.


def index(request):
    return render(request, 'index.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs':blogs})
