from django.contrib import admin
from .models import motd
# Register your models here.

@admin.register(motd)
class motdAdmin(admin.ModelAdmin):
    pass
