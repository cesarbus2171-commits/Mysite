from django.db import models

class usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    # ¡Borramos el class Meta con el managed = False!