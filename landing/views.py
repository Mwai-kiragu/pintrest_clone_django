from django.shortcuts import render
from django.http import HttpResponse
from .forms import RandomForm, LoginForm, RegisterForm


# Create your views here.


def home(request):

    fruits = ['apples', 'avs', 'mango', 'melon']
    
    context= {
        "title" : "My first Title",
        "login_form" : LoginForm(),
        "register_form" : RegisterForm(),
        "first_name": "Rey",
        "last_name": "Mysterio",
        "activity": "Best",
        "hobby": "Wrestler",
        "fruits": fruits,
    }

    return render(request, 'home.html', context)

    return HttpResponse("This is my page")

def about(request):

    context= {

        "title" :"My Second Title"
    }
    return render(request, 'about.html', context)

    return HttpResponse("This is Onesmus")