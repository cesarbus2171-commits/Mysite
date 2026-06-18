from django.db import models

# Create your models here.
class productos(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField()
    precio = models.DecimalField()
    stock = models.PositiveIntegerField()
    categoria = models.CharField()