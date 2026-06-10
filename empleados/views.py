from django.shortcuts import render
from django.http import HttpResponse


def empleados(request):

    #return HttpResponse("FORMULARIO DE EMPLEADOS CESAR")

    return render(request, 'empleados/empleados.html')