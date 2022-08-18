from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images/categorias")
    state = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)
