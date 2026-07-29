from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    color = models.CharField(max_length=50)
    precio = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)