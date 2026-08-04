from django.db import models

class Nomina(models.Model):
    numperiodo = models.CharField(max_length=50)
    fecha = models.DateField()
    salario = models.FloatField()
    percepciones = models.FloatField()
    deducciones = models.FloatField()
    total = models.FloatField()
    empleado = models.ForeignKey('empleados.Empleado', on_delete=models.CASCADE, related_name='nominas_registro')

    class Meta:
        db_table = 'nomina'