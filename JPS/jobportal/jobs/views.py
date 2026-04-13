from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from .forms import JobApplicationForm


# Register
def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered'})

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')


# Login
def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('job_list')

        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


# Logout
def user_logout(request):
    logout(request)
    return redirect('login')


# Dashboard
@login_required
def dashboard(request):

    jobs = Job.objects.all()

    return render(request, 'dashboard.html', {'jobs': jobs})


# Post Job
@login_required
def post_job(request):

    if request.method == "POST":

        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        description = request.POST['description']

        Job.objects.create(
            title=title,
            company=company,
            location=location,
            description=description,
            posted_by=request.user
        )

        return redirect('job_list')

    return render(request, 'post_job.html')


# Job List (Public)
def job_list(request):

    jobs = Job.objects.all()

    return render(request, 'job_list.html', {'jobs': jobs})


# Apply Job
@login_required
def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":

        form = JobApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()

            return redirect('job_list')

    else:
        form = JobApplicationForm()

    return render(request, 'apply_job.html', {'form': form, 'job': job})