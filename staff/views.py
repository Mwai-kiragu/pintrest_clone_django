from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse

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