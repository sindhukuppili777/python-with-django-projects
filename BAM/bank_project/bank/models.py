# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)