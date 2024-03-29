from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BlogForm, ProfileForm
from .models import Blog, Profile, Comment


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
    comments = Comment.objects.filter(post=blog).order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    context = {
        'blog': blog,
        "comments": comments,
        "profile": profile
    }
    return render(request, 'blog_detail.html', context)


def blog_delete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect("main:blog_list")


def blog_create(request):
    form = BlogForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("main:blog_list")
    return render(request, 'post_create.html', {"form": form})


def blog_update(request, pk):
    post = get_object_or_404(Blog, id=pk, author=request.user)
    form = BlogForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("main:blog_list")
    return render(request, 'post_update.html', {"form": form, 'post': post})


def create_comment(request, pk):
    post = get_object_or_404(Blog, id=pk)
    if request.method == "POST":
        data = request.POST
        Comment.objects.create(author=request.user, comment_text=data.get("comment"), post=post)
    return redirect("main:blog-detail", post.id)


def profile_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    posts = Blog.objects.filter(author=profile.user).order_by('-date')
    context = {
        "profile": profile,
        "posts": posts
    }
    return render(request, 'profile.html', context)


def profile_update(request, pk):
    profile = get_object_or_404(Profile, id=pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.user.first_name = form.cleaned_data['firstname']
            profile.user.last_name = form.cleaned_data['lastname']
            profile.user.save()
            profile.save()
            return redirect("main:profile-detail", pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {"form": form, "profile": profile})
