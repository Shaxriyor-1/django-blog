from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('search/', views.search, name='search'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('blog_create/', views.blog_create, name='blog-create'),
    path('blog_delete/<int:pk>/', views.blog_delete, name='blog-delete'),
    path('blog-update/<int:pk>/', views.blog_update, name='blog-update'),
    path('comment-create/<int:pk>/', views.create_comment, name='comment-create'),
    path('profile/<int:pk>/', views.profile_detail, name='profile-detail'),
    path('profile_update/<int:pk>/', views.profile_update, name='profile-update'),
]
