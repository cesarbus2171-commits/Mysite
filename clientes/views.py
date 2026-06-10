from django.shortcuts import render
from django.http import HttpResponse


def clientes(request):

    #return HttpResponse("FORMULARIO DE CLIENTES CESAR")

    return render(request, 'clientes/clientes.html')