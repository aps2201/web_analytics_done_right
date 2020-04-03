from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.


from .forms import customUserCreationForm, customUserChangeForm
from .models import customUser

class customUserAdmin(UserAdmin):
    model = customUser
    add_form = customUserCreationForm
    form = customUserChangeForm

admin.site.register(customUser, customUserAdmin)
