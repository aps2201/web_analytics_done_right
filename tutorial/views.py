from django.shortcuts import render
from .models import tutorial
from .models import subject
from .models import tutorial_menu

# Create your views here.
def index(request): 
    return render(request,
                  'tutorial/home.html',
                  {'page':'tutorial',
                    'tutorial':tutorial.objects.filter(subject__subject='utama'),
                    'menu':tutorial_menu.objects.all(),
                    })
                  
def detail(request,tutor_id):
    return render(request,
                  'tutorial/detail.html',
                  {'page':'tutorial',
                   'tutorial': tutorial.objects.get(tutor_id=tutor_id),
                   'menu': tutorial_menu.objects.all(),
                   })

def subject(request):
    return render(request,
                  'tutorial/subject.html',
                  {'page':'blog',
                   'subject': subject.objects.all()})
