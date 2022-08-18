from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from tablas.models import *

# Create your views here.

class CategoriaList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "tabla.view_categoria"
    model = Categoria
    template_name = "tabla/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"