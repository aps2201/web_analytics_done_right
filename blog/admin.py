from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import customUser
from .models import post
from .models import category


# Register your models here.

admin.site.register(customUser, UserAdmin)

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    pass

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    pass
