# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Student,Attendance
from datetime import date
from django.contrib.auth.models import User


# def home(request):
#     students = Student.objects.all()
#     return render(request,'home.html',{'students':students})


# def add_student(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         Student.objects.create(name=name,email=email)
#         return redirect('/')
#     return render(request,'add_student.html')


# def mark_attendance(request, id):
#     student = Student.objects.get(id=id)
#     Attendance.objects.create(
#         student=student,
#         date=date.today(),
#         status="Present"
#     )
#     return redirect('/')


# def view_attendance(request):
#     records = Attendance.objects.all()
#     return render(request,'attendance.html',{'records':records})


def login_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':'Invalid Login'})

    return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login')


@login_required
def home(request):
    students = Student.objects.all()
    return render(request,'home.html',{'students':students})


@login_required
def add_student(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        Student.objects.create(name=name,email=email)

        return redirect('/')

    return render(request,'add_student.html')


@login_required
def mark_attendance(request,id):

    student = Student.objects.get(id=id)

    today = date.today()

    already = Attendance.objects.filter(student=student,date=today).exists()

    if not already:
        Attendance.objects.create(
            student=student,
            date=today,
            status="Present"
        )

    return redirect('/')


@login_required
def view_attendance(request):

    records = Attendance.objects.all()

    return render(request,'attendance.html',{'records':records})



def register_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error':'Username already exists'})

        User.objects.create_user(username=username,email=email,password=password)

        return redirect('/login/')

    return render(request,'register.html')