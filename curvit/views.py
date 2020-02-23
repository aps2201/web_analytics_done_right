from django.shortcuts import render

# Create your views here.

page={'page':'curriculum vitae'}
def index(request):
    return render(request,
                  'curvit/home.html',
                  page)

def detail(request):
    return render(request,
                  'curvit/detail.html',
                  page)
