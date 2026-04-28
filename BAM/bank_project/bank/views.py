# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Account,Transaction
from .models import Account
import random

def register(request):
    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Generate Account Number
        account_number = "AC" + str(random.randint(100000,999999))

        # Create Bank Account
        Account.objects.create(
            user=user,
            account_number=account_number,
            balance=0
        )

        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'login.html')

def dashboard(request):
    account = Account.objects.get(user=request.user)
    return render(request,'dashboard.html',{'account':account})


# def dashboard(request):
#     account=Account.objects.filter(user=request.user).first()
#     return render(request,'dashboard.html',{'account':account})

def deposit(request):
    account, created = Account.objects.get_or_create(
        user=request.user,
        defaults={'account_number': 'ACC' + str(request.user.id), 'balance': 0}
    )

    if request.method == "POST":
        amount = float(request.POST['amount'])
        account.balance += amount
        account.save()

        Transaction.objects.create(
            account=account,
            transaction_type="Deposit",
            amount=amount
        )

        return redirect('dashboard')

    return render(request, 'deposit.html')

def withdraw(request):
    account = Account.objects.filter(user=request.user).first()

    if not account:
        return redirect('dashboard')

    if request.method == "POST":
        amount = float(request.POST['amount'])

        if account.balance >= amount:
            account.balance -= amount
            account.save()

            Transaction.objects.create(
                account=account,
                transaction_type="Withdraw",
                amount=amount
            )

        return redirect('dashboard')

    return render(request, 'withdraw.html')

def transaction_history(request):
    account=Account.objects.get(user=request.user)
    transactions=Transaction.objects.filter(account=account)
    return render(request,'transactions.html',{'transactions':transactions})

def user_logout(request):
    logout(request)
    return redirect('login')