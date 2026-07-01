from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'clientes_clientes'