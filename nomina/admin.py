from django.contrib import admin
from .models import Nomina

class NominaAdmin(admin.ModelAdmin):
    list_display= ('id', 'numperiodo', 'fecha', 'salario', 'percepciones', 'deducciones', 'total', 'empleado')
    search_fields= ('numperiodo', 'empleado')
    list_filter= ('numperiodo', 'empleado')
    ordering= ['numperiodo']

admin.site.register(Nomina, NominaAdmin)