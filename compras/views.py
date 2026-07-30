from django.shortcuts import render, redirect
from .models import compras

def listacompras(request):
    consultacompras = compras.objects.all()
    return render(request, 'compras/compras.html', {'consultacompras': consultacompras})

def creacompras(request):
    if request.method == 'POST':
        nuevo_compra = compras(
            folio=request.POST.get('folio'),
            fecha=request.POST.get('fecha'),
            subtotal=request.POST.get('subtotal'),
            iva=request.POST.get('iva'),
            total=request.POST.get('total')
        )
        nuevo_compra.save()
        return redirect('/pagecompras') 

    return render(request, 'compras/compras.html')