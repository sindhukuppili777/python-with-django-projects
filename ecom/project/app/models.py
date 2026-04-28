from django.db import models
from django.contrib.auth.models import User

# Create your models
class Products(models.Model):
    pname = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    pics =models.ImageField(upload_to='products',blank=True)

def __str__(self):
    return self.pname

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'{self.product.pname} x {self.quantity}'

