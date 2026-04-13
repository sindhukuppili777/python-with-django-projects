from django.urls import path
from . import views


urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
]

