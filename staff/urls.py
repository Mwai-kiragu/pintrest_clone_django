from django.contrib import admin
from django.urls import path
from .views import *
# from staff import views

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('users', viewUsers, name='users'),
    path('users/<id>', userDetails, name="user.details"),
    path('users/delete/<id>', deleteUser, name="user.delete"),
    # path('user/sendEmail', views.sendEmail, name='user.sendEmail'),
]