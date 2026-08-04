from django.shortcuts import render, redirect
from .models import Venta
from clientes.models import Cliente
from productos.models import Producto

def listaventas(request):
    consultaventas = Venta.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    
    return render(request, 'ventas/ventas.html', {
        'consultaventas': consultaventas,
        'clientes': clientes,
        'productos': productos
    })

def creaventa(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        total = request.POST.get('total')
        productos_ids = request.POST.getlist('productos')

        nueva_venta = Venta(
            cliente_id=cliente_id,
            total=total
        )
        nueva_venta.save()

        if productos_ids:
            nueva_venta.productos.set(productos_ids)

        return redirect('/pageventas/')
    
    return redirect('/pageventas/')