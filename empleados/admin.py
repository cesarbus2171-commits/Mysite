from django.contrib import admin
from .models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'apellido', 'sexo', 'puesto', 'departamento', 'estudios')
    search_fields= ('apellido', 'sexo')
    list_filter= ('sexo', 'puesto')
    ordering= ['apellido']

admin.site.register(Empleado, EmpleadoAdmin)