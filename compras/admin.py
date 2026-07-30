from django.contrib import admin
from .models import compras

class comprasAdmin(admin.ModelAdmin):
    list_display= ('id', 'folio', 'fecha', 'subtotal', 'iva', 'total')
    search_fields= ('folio', 'fecha')
    list_filter= ('subtotal', 'fecha')
    ordering= ['folio']

admin.site.register(compras, comprasAdmin)