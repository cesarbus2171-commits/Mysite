from django.contrib import admin
from .models import usuario

class UsuariosAdmin(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'apellido', 'sexo', 'tipo')
    search_fields= ('nombre', 'apellido')
    list_filter= ('sexo', 'tipo')
    ordering= ['nombre']

admin.site.register(usuario, UsuariosAdmin)

