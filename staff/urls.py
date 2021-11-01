from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
# from staff import views

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('users', viewUsers, name='users'),
    path('users/<id>', userDetails, name="user.details"),
    path('pins', PinList.as_view(), name="pins"),
    path('pin/create', CreatePin.as_view(), name="create.pin"),
    path('pin/update/<pk>', PinUpdate.as_view(), name="pin.update"),
    path('pin/<pk>/details', PinDetails.as_view(), name="pin.details"),
    path('boards', viewBoard, name='board'),
    path('comment', viewComment, name='comment'),
    path('comment/create', CreateComment.as_view(), name="create.comment"),
    path('comment/update/<pk>', CommentUpdate.as_view(), name="comment.update"),
    path('users/delete/<id>', deleteUser, name="user.delete"),
    path('board/create', CreateBoard.as_view(), name="create.board"),
    path('categories', CategoryList.as_view(), name="categories"),
    path('category/create', CreateCategory.as_view(), name="create.category"),
    path('category/update/<pk>', CategoryUpdate.as_view(), name="category.update"),
    # path('user/sendEmail', views.sendEmail, name='user.sendEmail'),
]   

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)