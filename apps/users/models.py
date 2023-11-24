from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    choices = (
        ('adminUser', 'adminUser'),
        ('user', 'user')
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    typeUser = models.CharField(
        max_length=50,
        choices = choices,
        blank=True
    )
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
