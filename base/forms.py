from django.contrib.auth.forms import UserCreationForm
from .models import User, Ticket
from django import forms

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username'] # Formularz rejestracji przyjmuje tylko pola email i username z modelu User

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'answer', 'image'] # Formularz zgłoszeniowy przyjmuje tylko te pola, które są w nawiasie i bierze je z modelu Ticket