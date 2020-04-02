from django.contrib import admin
from .models import general
from .models import experience
from .models import education
from .models import certification
from .models import volunteering

# Register your models here.

@admin.register(general)
class generalAdmin(admin.ModelAdmin):
    pass

@admin.register(experience)
class experienceAdmin(admin.ModelAdmin):
    pass

@admin.register(education)
class educationAdmin(admin.ModelAdmin):
    pass

@admin.register(certification)
class certificationAdmin(admin.ModelAdmin):
    pass

@admin.register(volunteering)
class volunteeringAdmin(admin.ModelAdmin):
    pass
