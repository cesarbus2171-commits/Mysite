from django.shortcuts import render, redirect
from .models import Producto



def listaproductos(request):
    consultaproductos= Producto.objects.all()
    return render(request, 'productos/productos.html', {'consultaproductos': consultaproductos})

def creaproductos(request):
    if request.method == 'POST':
        nuevo_producto = Producto(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            precio=request.POST.get('precio'),
            stock=request.POST.get('stock'),
            categoria=request.POST.get('categoria'),
            marca=request.POST.get('marca'),
            color=request.POST.get('color') 
        )
        nuevo_producto.save()
        return redirect('/pageproductos/')