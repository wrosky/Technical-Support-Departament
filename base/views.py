from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
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
            if user.is_technik == True: # Warunki dla, których użytkownik zostanie przekierowany na odpowiednią stronę
                login(request, user)
                return redirect('technik_dashboard')
            else:
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
            techniks = User.objects.filter(is_technik=True) # Warunek dla, którego zgłoszenie zostanie przypisane do technika, który ma najmniej zgłoszeń (kod aż do 60 linijki)
            min_tickets_technik = techniks[0]
            count = float('inf')
            for technik in techniks:
                technik_tickets = len(Ticket.objects.filter(technik=technik))
                if technik_tickets < count:
                    min_tickets_technik = technik
                    count = technik_tickets                   
            ticket.technik = min_tickets_technik 
            ticket.save()
            return redirect('customer_dashboard')
    else:
        form = TicketForm()
    return render(request, 'form.html', {'form': form})

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, Q(author=request.user) | Q(technik=request.user), ticket_id=ticket_id) # Warunek dla, którego użytkownik może edytować zgłoszenie tylko jeśli jest jego autorem lub technikiem, który je przyjął
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)      
            ticket.save()
            if request.user.is_technik == True:
                return redirect('technik_dashboard')
            else:
                return redirect('customer_dashboard')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'edit_ticket.html', {'form': form})

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id, author=request.user)
    ticket.delete()
    if request.user.is_technik == True:
        return redirect('technik_dashboard')
    else:
        return redirect('customer_dashboard')

@login_required
def change_ticket_status(request, ticket_id, new_status):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    if request.user.is_technik == True:
        ticket.status = new_status
        ticket.save()
        return redirect('technik_dashboard')
    else:
        return redirect('customer_dashboard')

@login_required
def ticket_stats(request):
    ticket_stats = Ticket.objects.values('status').annotate(total=Count('status')).order_by('status')

    return render(request, 'ticket_stats.html', {'ticket_stats': ticket_stats})

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

@login_required
def customer_dashboard(request):
    tickets = Ticket.objects.filter(author=request.user)
    return render (request, 'customer_dashboard.html', {'tickets': tickets})

@login_required
def technik_dashboard(request):
    tickets = Ticket.objects.filter(technik=request.user)
    return render (request, 'technik_dashboard.html', {'tickets': Ticket.objects.filter(technik=request.user)})

@login_required
def view_ticket(request, uuid):
    ticket = get_object_or_404(Ticket, ticket_id=uuid)
    return render (request, 'ticket_details.html', {'ticket': ticket})