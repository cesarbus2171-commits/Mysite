from django.db import models

class empleado(models.Model): 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    puesto = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    estudios = models.CharField(max_length=100)

class nomina(models.Model):
    numperiodo = models.CharField(max_length=50)
    fecha = models.DateField()
    salario = models.FloatField()
    perceciones = models.FloatField()
    deducciones = models.FloatField()
    total = models.FloatField()
    empleado = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name='nominas')