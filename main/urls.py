from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog-detail'),
]