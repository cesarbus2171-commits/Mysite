from django.contrib import admin
from .models import Grupo

class GrupoAdmin(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'descripcion', 'fecha_creacion', 'estatus')
    search_fields= ('nombre', 'estatus')
    list_filter= ('nombre', 'descripcion')
    ordering= ['nombre']

admin.site.register(Grupo, GrupoAdmin)