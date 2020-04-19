from django.contrib.sitemaps import Sitemap
from blog.models import post
from tutorial.models import tutorial


from django.urls import reverse

class blogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    
    def items(self):
        return post.objects.exclude(category__slug="hidden")
    
    def lastmod(self, obj):
        return obj.time_lastmodified


class tutorialSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    
    def items(self):
        return tutorial.objects.all()
    
    def lastmod(self, obj):
        return obj.time_lastmodified
    
class staticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home:index', 'blog:index', 'curvit:index']

    def location(self, item):
        return reverse(item)
