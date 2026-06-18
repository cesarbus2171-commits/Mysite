from django.db import models

# Create your models here.
class Proveedores(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    sexo = models.CharField()
    empresa = models.CharField()
    direccion = models.CharField()