from django.urls import path
from . import views

urlpatterns = [

    path('', views.feed, name='feed'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('upload/', views.upload_post, name='upload'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),

]

