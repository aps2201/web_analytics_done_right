from django.urls import path

from . import views

app_name='curvit'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.detail, name='cv-detail  '),
]
