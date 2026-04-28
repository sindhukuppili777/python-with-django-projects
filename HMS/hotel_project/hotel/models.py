from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return str(self.room_number)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return self.user.username