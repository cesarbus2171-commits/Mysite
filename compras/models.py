from django.db import models
from proveedores.models import proveedor 
from productos.models import producto

class compras(models.Model):
    folio = models.CharField(max_length=50)
    fecha = models.DateField()
    subtotal = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    # Relaciones de muchos a muchos:
    proveedor = models.ManyToManyField(proveedor)
    producto = models.ManyToManyField(producto)