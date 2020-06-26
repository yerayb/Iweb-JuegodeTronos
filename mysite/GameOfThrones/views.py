from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import  Temporada, Casa,Personaje

# Create your views here.



def index(request):
    personajesTargaryen = Personaje.objects.filter(casa=Casa.objects.get(nombre__iexact='Targaryen')).order_by('nombre').all()
    personajesStark = Personaje.objects.filter(casa=Casa.objects.get(nombre__iexact='Stark')).order_by('nombre').all()
    personajesBaratheon = Personaje.objects.filter(casa=Casa.objects.get(nombre__iexact='Baratheon')).order_by('nombre').all()
    personajesLannister = Personaje.objects.filter(casa=Casa.objects.get(nombre__iexact='Lannister')).order_by('nombre').all()
    personajesMartell = Personaje.objects.filter(casa=Casa.objects.get(nombre__iexact='Martell')).order_by('nombre').all()


    context = {
        'personajesTargaryen': personajesTargaryen,
        'personajesStark':  personajesStark,
        'personajesBaratheon':  personajesBaratheon,
        'personajesLannister':  personajesLannister,
        'personajesMartell':  personajesMartell,

    }

    return render(request, 'GameOfThrones/index.html', context)

def personaje(request):
    personaje = Personaje.objects.order_by('nombre')
    return render(request, 'GameOfThrones/personajes.html', {'personaje': personaje})

def casa(request):
    casas = Casa.objects.order_by('nombre')
    return render(request, 'GameOfThrones/casas.html', {'casas': casas})

def temporada(request):
    temporadas = Temporada.objects.order_by('num_temporada')
    return render(request, 'GameOfThrones/temporadas.html', {'temporadas': temporadas})

def personaje_detail(request, pk):
    personaje = get_object_or_404(Personaje, pk=pk)
    return render(request, 'GameOfThrones/personaje_detail.html', {'personaje': personaje})

def casa_detail(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    return render(request, 'GameOfThrones/casa_detail.html', {'casa':casa})

def temporada_detail(request, pk):
    temporada = get_object_or_404(Temporada, pk=pk)
    return render(request, 'GameOfThrones/temporada_detail.html', {'temporada': temporada})
