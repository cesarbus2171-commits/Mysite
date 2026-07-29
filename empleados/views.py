from django.shortcuts import render, redirect
from .models import Empleado

def listaempleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'empleados': empleados})

def creaempleado(request):
    if request.method == 'POST':
        nuevo = Empleado(
            nombre=request.POST.get('nombre'),
            puesto=request.POST.get('puesto'),
            salario=request.POST.get('salario'),
            fecha_ingreso=request.POST.get('fecha_ingreso'),
            email=request.POST.get('email')
        )
        nuevo.save()
        return redirect('/pageempleados/')
    return render(request, 'empleados/empleados.html')