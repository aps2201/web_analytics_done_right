from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import post
from .models import category


# Register your models here.
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    pass

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    pass
