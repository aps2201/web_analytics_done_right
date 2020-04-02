from django.urls import path
from django.urls import re_path

from . import views

app_name='service'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^product/(?P<item_id>.*)/$', views.detail, name='product-detail'),
]
