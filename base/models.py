import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# W modelu User jest opcja stowrzenia użytkownika, który może być albo klientem, albo technikiem
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=True)
    is_technik = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    pass

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('Send', 'Wysłane'),
        ('Open', 'Otwarte'),
        ('Reviewed', 'Ocenione'),
        ('Closed', 'Zamknięte'),
    )

    # Argumenty, które będą przekazywane do modelu Ticket, i z których będzie można korzystać w widokach
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    answer = models.TextField(max_length=2000, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Send')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    technik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='technik', null=True, blank=True)
    image = models.ImageField(upload_to='images/')