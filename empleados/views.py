from django.shortcuts import render, redirect
from .models import Empleado

def listaempleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'empleados': empleados})

def creaempleado(request):
    if request.method == 'POST':
        nuevo = Empleado(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            puesto=request.POST.get('puesto'),
            sexo=request.POST.get('sexo'),
            departamento=request.POST.get('departamento'),
            estudios=request.POST.get('estudios'),
        )
        nuevo.save()
        return redirect('/pageempleados/')
    return render(request, 'empleados/empleados.html')