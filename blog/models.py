from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse

import uuid

# Create your models here.

class customUser(AbstractUser):
    pass

class post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True,auto_now=False)
    time_lastmodified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('blog.category',null=True,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True,null=True)
    title = models.CharField(max_length = 50)
    content = models.TextField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:blog-post', args=[str(self.post_id)])
    
    class Meta:
        verbose_name_plural = "Blog Content"
        ordering = ['-time_lastmodified']

class category(models.Model):
    cat_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return reverse('blog:category', args=[str(self.cat_id)])
    class Meta:
        verbose_name_plural = "Category List"
    
