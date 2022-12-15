from django.urls import path

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.signup_view, name='signup'),

]
