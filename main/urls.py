from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('blog_create/', views.blog_create, name='blog-create'),
    path('blog_delete/<int:pk>/', views.blog_delete, name='blog-delete'),
]
