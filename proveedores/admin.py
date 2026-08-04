from django.contrib import admin
from .models import proveedor

class ProveedoresAdmin(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'apellido', 'sexo', 'empresa', 'direccion')
    search_fields= ('nombre', 'apellido')
    list_filter= ('sexo', 'empresa')
    ordering= ['nombre']

admin.site.register(proveedor, ProveedoresAdmin)