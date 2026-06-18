from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField()
    precio = models.DecimalField()
    stock = models.PositiveIntegerField()
    categoria = models.CharField()