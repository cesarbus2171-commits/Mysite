from django.db import models

# Create your models here.
class empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    puesto = models.CharField(max_length=100)
    edad = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'empleados_empleados'
