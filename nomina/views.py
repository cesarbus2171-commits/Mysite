from django.shortcuts import render, redirect
from .models import Nomina
from empleados.models import Empleado

def listanominas(request):
    nominas = Nomina.objects.all()
    lista_empleados = Empleado.objects.all()
    return render(request, 'nomina/nomina.html', {'nominas': nominas, 'empleados': lista_empleados})

def creanominas(request):
    if request.method == 'POST':
        nueva_nomina = Nomina(
            numperiodo=request.POST.get('numperiodo'),
            fecha=request.POST.get('fecha'),
            salario=request.POST.get('salario'),
            percepciones=request.POST.get('percepciones'),
            deducciones=request.POST.get('deducciones'),
            total=request.POST.get('total'),
            empleado_id=request.POST.get('empleado')
        )
        nueva_nomina.save()
        return redirect('/pagenominas/')
    return render(request, 'nomina/nomina.html')