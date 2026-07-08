from django.shortcuts import render, redirect
from .models import Cliente
from clientes import models


def listaclientes(request):
    consultaclientes= Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'consultaclientes': consultaclientes})

def creaclientes(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        sexo = request.POST.get('sexo')
        tipo = request.POST.get('tipo')
        direccion = request.POST.get('direccion')

        # Creamos y guardamos el nuevo objeto
        nuevo_cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            sexo=sexo,
            tipo=tipo,
            direccion=direccion
        )
        nuevo_cliente.save()
        
        # Redirigimos a una página de confirmación o de vuelta al formulario
        return redirect('/pageclientes/') 
    
    return render(request, 'clientes/clientes.html')