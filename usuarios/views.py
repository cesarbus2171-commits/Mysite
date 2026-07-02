from django.shortcuts import render, redirect
from .models import usuario



def listausuarios(request):
    consultausuarios= usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'consultausuarios': consultausuarios})

def creausuario(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        sexo = request.POST.get('sexo')
        tipo = request.POST.get('tipo')

        # Creamos y guardamos el nuevo objeto
        nuevo_usuario = usuario(
            nombre=nombre,
            apellido=apellido,
            sexo=sexo,
            tipo=tipo
        )
        nuevo_usuario.save()
        return redirect('/pageusuarios/')