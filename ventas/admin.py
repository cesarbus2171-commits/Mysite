from django.contrib import admin
from .models import Venta

class VentasAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'mostrar_productos', 'fecha_venta', 'total')
    search_fields = ('cliente__nombre', 'cliente__apellido')
    list_filter = ('fecha_venta',)
    ordering = ['fecha_venta']

    def mostrar_productos(self, obj):
        return ", ".join([producto.nombre for producto in obj.productos.all()])
    
    mostrar_productos.short_description = 'Productos'

admin.site.register(Venta, VentasAdmin)