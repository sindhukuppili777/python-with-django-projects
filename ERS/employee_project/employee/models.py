from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.name