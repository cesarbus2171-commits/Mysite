from django.shortcuts import render, redirect
from .models import Venta
from clientes.models import Cliente
from productos.models import Producto

def listaventas(request):
    consultaventas = Venta.objects.all()
    return render(request, 'ventas/ventas.html', {'consultaventas': consultaventas})

def creaventa(request):
    if request.method == 'POST': 
        cliente_id = request.POST.get('cliente')
        total = request.POST.get('total')
        productos_ids = request.POST.getlist('productos')  

        # Crear la venta
        nueva_venta = Venta(  # ✅ SIN ESPACIOS
            cliente_id=cliente_id,
            total=total
        )
        nueva_venta.save()

        # Asignar productos (ManyToMany)
        if productos_ids:
            nueva_venta.productos.set(productos_ids)

        return redirect('/pageventas/')

    # Si es GET, mostrar formulario
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'ventas/creaventa.html', {
        'clientes': clientes,
        'productos': productos,
    })