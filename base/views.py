from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .form import RegisterCustomerForm, YourForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterCustomerForm()
        return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')
        else:
            return render(request, 'home.html', {'error': 'Nieprawidłowa nazwa użytkownika lub hasło'})
    else:
        return render(request, 'home.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def form_user(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Zastąp 'home' nazwą widoku, do którego chcesz przekierować po zapisaniu formularza
    else:
        form = YourForm()
    return render(request, 'form.html', {'form': form})

def home(request):
    return render (request, 'home.html')

def register(request):
    return render (request, 'register.html')

def form(request):
    return render (request, 'form.html')

def dashboard(request):
    return render (request, 'dashboard.html')

def customer_dashboard(request):
    return render (request, 'customer_dashboard.html')