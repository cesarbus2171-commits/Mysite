from django.shortcuts import render
from django.http import HttpResponse


def proveedores(request):

    #return HttpResponse("FORMULARIO DE PROVEEDORES CESAR")

    return render(request, 'proveedores/proveedores.html')