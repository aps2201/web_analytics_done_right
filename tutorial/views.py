from django.shortcuts import render
from .models import tutorial
from .models import subject
from .models import tutorial_menu

# Create your views here.
def index(request): 
    return render(request,
                  'tutorial/home.html',
                  {'page':'tutorial',
                    'tutorial':tutorial.objects.get(subject__subject='utama'),
                    'menu':tutorial_menu.objects.all(),
                    'menu_items': tutorial_menu.objects.get(tutorial__subject__subject='utama'),
                    })
                  
def detail(request,slug):
    return render(request,
                  'tutorial/detail.html',
                  {'page':'tutorial',
                   'tutorial': tutorial.objects.get(slug=slug),
                   'menu': tutorial_menu.objects.all(),
                   'menu_items': tutorial_menu.objects.get(tutorial__slug=slug),
                   })

def subject(request):
    return render(request,
                  'tutorial/subject.html',
                  {'page':'blog',
                   'subject': subject.objects.all()})
