from django.shortcuts import render
from django.http import HttpResponse


def productos(request):

    #return HttpResponse("FORMULARIO DE PRODUCTOS CESAR")

    return render(request, 'productos/productos.html')