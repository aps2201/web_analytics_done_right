from django.shortcuts import render
from .models import motd
from datetime import datetime
# Create your views here.
page={'page':'home'}
def index(request):
    return render(request,
                  'home/home.html',
                  {'page':'home',
                   'motd':motd.objects.latest('time_lastmodified'),})
