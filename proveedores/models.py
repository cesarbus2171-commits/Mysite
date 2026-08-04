from django.db import models

class proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    empresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    