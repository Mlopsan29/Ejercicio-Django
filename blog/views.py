from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

# Create your views here.

# Vista para la lista de animales

from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

# 1. Vista de Animales
def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'blog/lista_animales.html', {'animales': animales})

# 2. Vista de Protectoras
def lista_protectoras(request):
    protectoras = Protectora.objects.all()
    return render(request, 'blog/lista_protectoras.html', {'protectoras': protectoras})

# 3. Vista de Colaboradores
def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'blog/lista_colaboradores.html', {'colaboradores': colaboradores})