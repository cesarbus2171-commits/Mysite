from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    class Meta:
        managed = False     
        db_table = 'usuarios_usuarios'