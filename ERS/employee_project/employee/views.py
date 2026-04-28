
# Create your views here.
from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employee_list.html',{'employees':employees})


def add_employee(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        department = request.POST['department']
        salary = request.POST['salary']

        Employee.objects.create(
            name=name,
            email=email,
            phone=phone,
            department=department,
            salary=salary
        )
        return redirect('/')

    return render(request,'add_employee.html')


def delete_employee(request,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login/')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'Invalid Credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')