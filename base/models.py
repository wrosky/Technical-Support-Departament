from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=True)
    is_technik = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    pass

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('send', 'Wysłane'),
        ('open', 'Otwarte'),
        ('reviewed', 'Ocenione'),
        ('closed', 'Zamknięte'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='send')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')