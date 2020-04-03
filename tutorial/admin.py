from django.contrib import admin
from .models import tutorial
from .models import subject
from .models import tutorial_menu
# Register your models here.

@admin.register(tutorial)
class tutorialAdmin(admin.ModelAdmin):
    pass

@admin.register(subject)
class subjectAdmin(admin.ModelAdmin):
    pass

@admin.register(tutorial_menu)
class menuAdmin(admin.ModelAdmin):
    pass
