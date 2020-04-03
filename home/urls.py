from django.urls import path

from . import views

app_name='home'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/login/',views.login_page, name='login'),
    path('logout/',views.logout_, name='logout'),
]
