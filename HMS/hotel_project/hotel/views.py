# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Booking
from django.contrib import messages

def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request,'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user:
            login(request,user)
            return redirect('rooms')

    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def rooms(request):
    data = Room.objects.all()
    return render(request,'rooms.html',{'rooms':data})



def book_room(request,id):

    room = Room.objects.get(id=id)

    if request.method == "POST":

        checkin = request.POST['checkin']
        checkout = request.POST['checkout']

        # check booking conflict
        exists = Booking.objects.filter(
            room=room,
            checkin__lt=checkout,
            checkout__gt=checkin
        ).exists()

        if exists:
            messages.error(request,"Room already booked for selected dates")
            return redirect('rooms')

        Booking.objects.create(
            user=request.user,
            room=room,
            checkin=checkin,
            checkout=checkout
        )

        return redirect('rooms')

    return render(request,'booking.html',{'room':room})


def my_bookings(request):

    bookings = Booking.objects.filter(user=request.user)

    return render(request,'mybookings.html',{'bookings':bookings})