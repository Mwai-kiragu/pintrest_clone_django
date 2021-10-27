from django.contrib import admin
from django.urls import path
from .views import *
# from staff import views

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('users', viewUsers, name='users'),
    path('users/<id>', userDetails, name="user.details"),
    path('pin', viewPin, name='pin'),
    path('boards', viewBoard, name='board'),
    path('comment', viewComment, name='comment'),
    path('users/delete/<id>', deleteUser, name="user.delete"),
    path('board/create', CreateBoard.as_view(), name="create.board")
    # path('user/sendEmail', views.sendEmail, name='user.sendEmail'),
]   