from django.db import models

# Create your models here.
class productos(models.Model):
    nombre = models.CharField()
    descripcion = models.CharField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categorias= models.CharField()