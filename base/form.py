from django.contrib.auth.forms import UserCreationForm
from .models import User, Submission
from django import forms

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']

class YourForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'description', 'image']