from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
   	path('logout', auth_views.logout_then_login, name="logout"),
]