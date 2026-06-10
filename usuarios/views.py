from django.shortcuts import render
from django.http import HttpResponse


def usuarios(request):

    #return HttpResponse("FORMULARIO DE USUARIOS CESAR")

    return render(request, 'usuarios/usuarios.html')