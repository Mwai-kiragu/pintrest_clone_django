from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import RandomForm, LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail


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

def registerUser(request):
    
    if request.method == "GET":

        data = {
            'success': False, 
            'message':"Should be a post request."
            }
        return JsonResponse(data)

    else:

        form = RegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User()
            user.username = name
            user.age = age
            user.email = email
            user.set_password(password)
            user.save()

            login(request, user)
            mail_message = "Hello, "+name+" .Welcome to our very own Pintrest Clone. Jibambe Msee."            
            send_mail(
                'Welcome to PinClone',
                mail_message,
                "admin@gmail.com",
                [email],
                fail_silently= False
            )

        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        data = {'success': True, 'message':"Register Successful, Redirecting..."}
        return JsonResponse(data)

def loginUser(request):
    
    if request.method == 'GET':
        HttpResponse("Go home")

    else:

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                context = {}


                return HttpResponseRedirect('/user/profile')
            else:
                messages.error(request, 'Login not Successful')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def profile(request):
    context={}

    return render(request, 'profile.html', context)

def logout(request):

    logout(request)

    return HttpResponseRedirect('/')

