from django.urls import path
from . import views

urlpatterns = [

path('login/',views.login_page,name='login'),
path('logout/',views.logout_page,name='logout'),
path('register/',views.register_page,name='register'),

path('',views.home),
path('add/',views.add_student),
path('mark/<int:id>/',views.mark_attendance),
path('attendance/',views.view_attendance),

]