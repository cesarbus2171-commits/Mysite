from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categorias= models.CharField(max_length=100)
    class Meta:
        managed = False     
        db_table = 'productos_productos'