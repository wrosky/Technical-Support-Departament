from django.contrib.auth.forms import UserCreationForm
from .models import User, Ticket
from django import forms

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']