from django.urls import path,re_path

from . import views

app_name='blog'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^post/(?P<post_id>.*)/$', views.detail, name='blog-post'),
    path('category/', views.category, name='blog-category'),
]
