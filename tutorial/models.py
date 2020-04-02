from django.db import models

# Create your models here.
import uuid

class tutorial(models.Model):
    tutor_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time_created = models.DateTimeField(auto_now_add=True,auto_now=False)
    time_lastmodified = models.DateTimeField(auto_now=True)
    subject = models.ForeignKey('tutorial.subject',null=True,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True,null=True)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    menu = models.OneToOneField('tutorial.tutorial_menu', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tutorial:tutorial', args=[str(self.tutor_id)])
    
    class Meta:
        verbose_name_plural = "Tutorial Content"
        ordering = ['-time_lastmodified']

class subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=255)
    keywords = models.TextField(null=True)
    slug = models.SlugField(max_length=100,unique=True,null=True)
    
    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return reverse('blog:category', args=[str(self.cat_id)])
    
    def save(self, *args, **kwargs):
        value = self.subject
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class tutorial_menu(models.Model):
    menu_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255,null=True)
    items=models.TextField(null=True)
    position=models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Tutorial Menu"
        ordering = ['position']
