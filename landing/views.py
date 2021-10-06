from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    context= {
        "title" : "My first Title"
    }

    return render(request, 'home.html', context)

    return HttpResponse("This is my page")

def about(request):

    context= {
        "title" :"My Second Title"
    }
    return render(request, 'about.html', context)

    return HttpResponse("This is Onesmus")