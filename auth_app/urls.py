from django.urls import path, include

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('', include("django.contrib.auth.urls") ),

]
