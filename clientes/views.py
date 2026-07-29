from django.shortcuts import render, redirect
from .models import Cliente

def listaclientes(request):
    consultaclientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'consultaclientes': consultaclientes})

def creaclientes(request):
    if request.method == 'POST':
        nuevo_cliente = Cliente(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            sexo=request.POST.get('sexo'),
            tipo=request.POST.get('tipo'),
            direccion=request.POST.get('direccion')
        )
        nuevo_cliente.save()
        return redirect('/pageclientes/') 
    
    return render(request, 'clientes/clientes.html')