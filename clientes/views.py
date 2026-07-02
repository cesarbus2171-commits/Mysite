from django.shortcuts import render, redirect
from .models import cliente
from clientes import models


def listaclientes(request):
    consultaclientes= cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'consultaclientes': consultaclientes})

def creaclientes(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        print("DATOS RECIBIDOS:", request.POST)

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        sexo = request.POST.get('sexo')
        tipo = request.POST.get('tipo')
        direccion = request.POST.get('direccion')

        # Creamos y guardamos el nuevo objeto
        nuevo_cliente = cliente(
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