from django.shortcuts import render
from .models import post
# Create your views here.

page={'page':'blog'}
def index(request): 
    return render(request,
                  'blog/home.html',
                  {'page':'blog',
                    'post':post.objects.exclude(category__slug='hidden'),
                    })

def detail(request,post_id):
    return render(request,
                  'blog/detail.html',
                  {'page':'blog',
                   'post': post.objects.get(post_id=post_id),
                   })

def category(request):
    return render(request,
                  'blog/category.html',
                  {'page':'blog',
                   'post_cat': post.category.objects.all()})
