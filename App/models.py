# MiApp/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
