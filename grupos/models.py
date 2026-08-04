from django.db import models

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])

    class Meta:
        db_table = 'grupos_grupos'

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    correo = models.EmailField()
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='usuarios')