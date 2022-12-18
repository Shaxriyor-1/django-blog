from django.urls import path, include

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('password/', views.PasswordsChangeView.as_view(), name='password_change'),
    path('password_success/', views.password_change_success, name='password_success'),
    path('password_reset/', views.password_reset, name='password_reset'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('signup/', views.signup, name='signup'),
]
