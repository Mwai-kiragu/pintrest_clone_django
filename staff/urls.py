from django.contrib import admin
from django.urls import path
from .views import *
# from staff import views

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    # path('user/sendEmail', views.sendEmail, name='user.sendEmail'),
]