from django.shortcuts import render
from .models import general,experience,education,certification,volunteering

# Create your views here.

page={'page':'curriculum vitae'}
def index(request):
    return render(request,
                  'curvit/home.html',
                  {'page':'curriculum vitae',
                   'general':general.objects.get(first_name='Andaru'),
                   'experience':experience.objects.filter(cv__first_name='Andaru'),
                   #'education':education.objects.all(),
                   'certification':certification.objects.filter(cv__first_name='Andaru'),
                   #'volunteering':volunteering.objects.all(),
                   })

def detail(request):
    return render(request,
                  'curvit/detail.html',
                  page)
