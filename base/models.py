from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=True)
    is_technik = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    pass

class Submission(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='submissions/')