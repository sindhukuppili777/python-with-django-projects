from django.contrib import admin
from django.urls import path
from bank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='home'),   # ADD THIS LINE
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('transactions/', views.transaction_history, name='transactions'),
    path('logout/', views.user_logout, name='logout'),
    
]