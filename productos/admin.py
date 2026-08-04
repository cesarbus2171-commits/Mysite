from django.contrib import admin
from .models import Producto

class ProductosAdmin(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'marca', 'color')
    search_fields= ('nombre', 'categoria')
    list_filter= ('categoria', 'marca')
    ordering= ['nombre']

admin.site.register(Producto, ProductosAdmin)