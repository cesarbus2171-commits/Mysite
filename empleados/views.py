from django.shortcuts import render, redirect
from .models import empleado
from clientes import models


def listaempleados(request):
    consultaempleados= empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'consultaempleados': consultaempleados})

def creaempleados(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        sexo = request.POST.get('sexo')
        puesto = request.POST.get('puesto')
        edad = request.POST.get('edad')

        # Creamos y guardamos el nuevo objeto
        nuevo_empleado = empleado(
            nombre=nombre,
            apellido=apellido,
            sexo=sexo,
            puesto=puesto,
            edad=edad
        )
        nuevo_empleado.save()
        return redirect('/pageempleados/')