from django.shortcuts import render, redirect
from .models import clientes


def listaclientes(request):

    return render(request, 'clientes/clientes.html')

def creaclientes(request):
    if request.method == 'POST':
        nvocliente = clientes(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            sexo=request.POST['sexo'],
            tipo=request.POST['tipo'],
            direccion=request.POST['direccion']
        )
        nvocliente.save()
        return redirect('/pageclientes/')