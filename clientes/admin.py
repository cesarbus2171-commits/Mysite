from django.contrib import admin
from .models import Cliente

class ClientesAdmin(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'apellido', 'sexo', 'tipo', 'direccion')
    search_fields= ('apellido', 'sexo')
    list_filter= ('sexo', 'tipo')
    ordering= ['apellido']

admin.site.register(Cliente, ClientesAdmin)