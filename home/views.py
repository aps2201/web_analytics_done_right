from django.shortcuts import render
from django.shortcuts import redirect

from .models import motd
from datetime import datetime
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
# Create your views here.
page={'page':'home'}
def index(request):
    return render(request,
                  'home/home.html',
                  {'page':'home',
                   'motd':motd.objects.latest('time_lastmodified'),})
def login_page(request):
    return render(request,
                  'registration/login.html',
                  {'page':'home',
                   })
def login_(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        

def logout_(request):
    logout(request)
    return redirect('home:index')
