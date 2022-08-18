from django.urls import path
from tablas.views import *

app_name = "tablas"
urlpatterns = [
    path('categorias/', CategoriaList.as_view(), name="categoria_list"),
]
