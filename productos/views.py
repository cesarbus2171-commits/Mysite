from django.shortcuts import render, redirect
from .models import Producto



def listaproductos(request):
    consultaproductos= Producto.objects.all()
    return render(request, 'productos/productos.html', {'consultaproductos': consultaproductos})

def creaproductos(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario

        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categorias = request.POST.get('categorias')

        # Creamos y guardamos el nuevo objeto
        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categorias=categorias
        )
        nuevo_producto.save()
        return redirect('/pageproductos/')