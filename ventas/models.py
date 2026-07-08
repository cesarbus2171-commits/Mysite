from django.db import models
from clientes.models import Cliente
from productos.models import Producto 

class Venta(models.Model):
    # Aquí está tu relación de 1 a Muchos con Clientes:
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    # ¡Y aquí está tu relación Muchos a Muchos con Productos!
    productos = models.ManyToManyField(Producto) 
    
    fecha_venta = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'ventas_venta'