from django.db import models
from apps.users.models import User
from apps.address.models import Address
from apps.product.models import Product

# Create your models here.

class Request(models.Model):

    value = models.FloatField(blank=True)
    user = models.ForeignKey(User, related_name='user_requesst', blank=True, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, related_name='resque_address',blank=True, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):

        return self.user
    
class ProductRequest(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    quantity = models.IntegerField()



    