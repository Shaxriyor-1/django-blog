from django.contrib.auth.views import PasswordChangeView, LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views import generic

from auth_app.forms import SignUpForm, ChangePasswordForm, LoginForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('auth_app:login')


class PasswordsChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('auth_app:password_success')


def password_change_success(request):
    return render(request, 'registration/password_change_done.html', {})


def password_reset(request):
    pass


class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('main:blog_list')


# def dashboard(request):
#     return render(request, 'auth_app/dashboard.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('auth_app:dashboard')
#     else:
#         form = UserCreationForm()
#     return render(request, 'auth_app/signup.html', {'form':form})