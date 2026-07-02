from django.shortcuts import render, redirect
from .models import proveedor



def listaproveedores(request):
    consultaproveedores= proveedor.objects.all()
    return render(request, 'proveedores/proveedores.html', {'consultaproveedores': consultaproveedores})

def creaproveedor(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        sexo = request.POST.get('sexo')
        empresa = request.POST.get('empresa')
        direccion = request.POST.get('direccion')

        # Creamos y guardamos el nuevo objeto
        nuevo_proveedor = proveedor(
            nombre=nombre,
            apellido=apellido,
            sexo=sexo,
            empresa=empresa,
            direccion=direccion
        )
        nuevo_proveedor.save()
        return redirect('/pageproveedores/')