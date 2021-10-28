from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from landing.models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

def dashboard(request):

    context = {
        'users': User.objects.all(),

    }

    return render(request, 'dashboard.html', context)

def viewUsers(request):
    context = {
        'users' : User.objects.all()
    }

    return render(request, 'users.html', context)


def userDetails(request, id):

    user= User.objects.get(pk = id)
    context = {
        'user': user
    }

    return render(request, 'user_details.html', context)

def deleteUser(request, id):
    user= User.objects.get(pk = id)

    user.delete()

    if request.is_ajax():
        data = {}
        return JsonResponse(data)

    else:
        return HttpResponseRedirect('/staff/users')

def viewPin(request):
    context = {
        'pin' : Pin.objects.all()
    }

    return render(request, 'pin.html', context)

def viewBoard(request):
    context = {
        'boards' : Board.objects.all()
    }

    return render(request, 'board.html', context)

def viewComment(request):
    context = {
        'comment' : Comment.objects.all()
    }

    return render(request, 'comment.html', context)

class CreateBoard(CreateView):
    model = Board
    fields = '__all__'
    success_url = '/staff/boards'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Board"
        return context

class CategoryList(ListView):
    model = Category
    context_object_name  ="categoriess"
    template_name = 'categories.html'

class CreateCategory(CreateView):
    model = Category
    fields = ['name']
    success_url = '/staff/categories'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Category"
        return context

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name']
    success_url = '/staff/categories'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Category"
        return context

class PinList(ListView):
    model = Pin
    context_object_name  = "pins"
    template_name = 'pin.html'

class CreatePin(CreateView):
    model = Pin
    fields = '__all__'
    success_url = '/staff/pins'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Pin"
        return context

class PinUpdate(UpdateView):
    model = Pin
    fields = '__all__'
    success_url = '/staff/pins'
    template_name = 'board_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Pin"
        return context
