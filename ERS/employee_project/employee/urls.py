from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list),
    path('add/', views.add_employee),
    path('delete/<int:id>/', views.delete_employee),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
