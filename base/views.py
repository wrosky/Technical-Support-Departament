from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterCustomerForm, TicketForm
from .models import User, Ticket

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
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            return redirect('customer_dashboard')  # Zastąp 'home' nazwą widoku, do którego chcesz przekierować po zapisaniu formularza
    else:
        form = TicketForm()
    return render(request, 'form.html', {'form': form})

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, author=request.user)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            return redirect('customer_dashboard')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'edit_ticket.html', {'form': form})

@login_required
def tickets_list(request):
    tickets = Ticket.objects.filter(author=request.user)
    return render(request, 'dashboard.html', {'tickets': tickets})

def home(request):
    return render (request, 'home.html')

def register(request):
    return render (request, 'register.html')

def form(request):
    return render (request, 'form.html')

def dashboard(request):
    return render (request, 'dashboard.html')

def customer_dashboard(request):
    tickets = Ticket.objects.filter(author=request.user)
    return render (request, 'customer_dashboard.html', {'tickets': tickets})

def view_ticket(request, uuid):
    ticket = get_object_or_404(Ticket, ticket_id=uuid)
    return render (request, 'ticket_details.html', {'ticket': ticket})