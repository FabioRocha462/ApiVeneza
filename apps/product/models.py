from django.db import models

# Create your models here.

class Product(models.Model):
    choices = (
        ('Pizza', 'Pizza'),
        ('Esphira', 'Esphira'),
        ('Bebidas', 'Bebidas')
    )
    name = models.CharField(max_length=255)
    value = models.FloatField(null=True, blank=True)
    typeProduct = models.CharField(
        max_length= 50,
        choices= choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name