from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def dashboard(request):
    return render(request, 'auth_app/dashboard.html')

def signup_view(request):
    form = UserCreationForm()
    return render(request, 'auth_app/signup.html', {'form':form})