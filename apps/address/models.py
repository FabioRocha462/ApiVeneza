from django.db import models
from apps.users.models import User
# Create your models here.

class Address(models.Model):

    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    number = models.CharField(max_length=50)
    referencePoint = models.TextField(max_length= 500)
    user = models.ForeignKey(User,related_name="user_address", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):

        return self.user

