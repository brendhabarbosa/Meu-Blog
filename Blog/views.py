from django.shortcuts import render
from .models import Cursos, Habilidade
# Create your views here.
def index(request):
    habilidades = Habilidade.objects.all()
    cursos = Cursos.objects.all()
    context = {
        'habilidades': habilidades,
        'cursos': cursos
    }
    return render(request, 'blog/index.html', context)

def sobre(request):
    habilidades = Habilidade.objects.all()
    cursos = Cursos.objects.all()
    context = {
        'habilidades': habilidades,
        'cursos': cursos
    }
    return render(request, 'blog/sobre.html', context)