from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BlankView(LoginRequiredMixin, TemplateView):
    template_name = "bases/home.html"
    login_url = 'bases:login'
