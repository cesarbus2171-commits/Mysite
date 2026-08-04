from django.shortcuts import render, redirect
from .models import Grupo

def listagrupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupos/grupos.html', {'grupos': grupos})

def creagrupos(request):
    if request.method == 'POST':
        nuevo = Grupo(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            estatus=request.POST.get('estatus')
        )
        nuevo.save()
        return redirect('/pagegrupos/')
    return render(request, 'grupos/grupos.html')