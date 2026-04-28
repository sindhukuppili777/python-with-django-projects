from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.handlelogin, name="login"),
    path('products', views.products, name="products"),
    path('cart', views.cart, name="cart"),
    path('search', views.search, name="search"),
    path('vcart/<id>/', views.addcart, name="addcart"),
    path('dcart/<id>/', views.delcart, name="delcart"),
    path('signup', views.handlesignup, name="signup"),
    path('logout', views.handlelogout, name="logout"),
]