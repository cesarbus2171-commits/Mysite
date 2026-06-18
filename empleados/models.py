from django.db import models

# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    sexo = models.CharField()
    puesto = models.CharField()
    edad = models.CharField()