"""wadr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap

app_name='wadr'

from home.sitemaps import blogSitemap,staticSitemap,tutorialSitemap
sitemaps = {
    "posts": blogSitemap,
    "tutorial": tutorialSitemap,
    "static": staticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('',include('home.urls'),name='home'),
    path('blog/',include('blog.urls'),name='blog'),
    path('cv/',include('curvit.urls'),name='curvit'),
    path('service/',include('service.urls'),name='service'),
    path('wadr/',include('tutorial.urls'),name='tutorial'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),


]
