from django.shortcuts import render
from .models import Socio, Entrenador, Clase
# Create your views here.

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'gimnasio/lista_socios.html', {'socios': socios})

def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'gimnasio/lista_entrenadores.html' , {'entrenadores': entrenadores})

def lista_clases(request):
    clases = Clase.objects.all()
    return render(request, 'gimnasio/lista_clases.html', {'clases': clases})