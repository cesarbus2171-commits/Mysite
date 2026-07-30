from django.contrib import admin
from .models import Empleado

class empleadoAdmin(admin.ModelAdmin):
    list_display= ()
    search_fields= ()
    list_filter= ()
    ordering= []

admin.site.register(Empleado, empleadoAdmin)