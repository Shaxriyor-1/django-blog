from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

def dashboard(request):
    return render(request, 'auth_app/dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('auth_app:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'auth_app/signup.html', {'form':form})