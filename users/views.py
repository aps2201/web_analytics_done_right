from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import customUserCreationForm

class SignUpView(CreateView):
    form_class = customUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
