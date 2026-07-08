from django.db import models

# Create your models here.
class Producto(models.Model): # <--- ¡P mayúscula aquí!
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    peso = models.FloatField() 
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    color = models.CharField(max_length=50)