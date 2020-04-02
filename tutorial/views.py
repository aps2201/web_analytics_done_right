from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request,
                  'tutorial/home.html',
                  {'page':'tutorial',
                    'tutorial':tutorial.objects.get(subject='utama'),
                    #'menu':tutorial.menu.objects.all(),
                    })
                  
def detail(request,tutor_id):
    return render(request,
                  'tutorial/detail.html',
                  {'page':'tutorial',
                   'tutorial': tutorial.objects.get(tutor_id=tutor_id),
                   'menu': tutorial.menu.objects.all(),
                   })

def subject(request):
    return render(request,
                  'tutorial/subject.html',
                  {'page':'blog',
                   'subject': tutorial.subject.objects.all()})
