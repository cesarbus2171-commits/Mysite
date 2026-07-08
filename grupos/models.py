from django.db import models

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)

    class Meta:
        db_table = 'grupos_grupos'

class UsuarioGrupo(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    correo = models.EmailField()
    # Clave foránea para relacionarlo con el grupo
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'grupos_usuarios'