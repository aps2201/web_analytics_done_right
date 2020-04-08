from django.urls import path,re_path

from . import views

app_name='tutorial'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^tutorial/(?P<slug>.*)/$', views.detail, name='tutorial'),
    path('subject/', views.subject, name='tutorial-subject'),
]

