from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.contrib import messages
from .models import Post
from django.shortcuts import redirect, get_object_or_404

# REGISTER
def register_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'core/register.html')


# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'core/login.html')


# Login
# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('login')


# FEED PAGE
@login_required
def feed(request):

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'core/feed.html', {'posts': posts})


# UPLOAD POST
@login_required
def upload_post(request):

    if request.method == "POST":

        image = request.FILES.get('image')
        caption = request.POST.get('caption')

        if image:
            Post.objects.create(
                user=request.user,
                image=image,
                caption=caption
            )

        return redirect('feed')

    return render(request, 'core/upload.html')


# COMMENT
@login_required
def comment(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == "POST":

        text = request.POST.get('text')

        Comment.objects.create(
            post=post,
            user=request.user,
            text=text
        )

    return redirect('feed')


# PROFILE PAGE
@login_required
def profile(request, username):

    user_profile = User.objects.get(username=username)

    posts = Post.objects.filter(user=user_profile)

    return render(request, 'core/profile.html', {
        'user_profile': user_profile,
        'posts': posts
    })

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('feed')



def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')