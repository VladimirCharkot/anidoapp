from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'blog/index.html', {})
#	return HttpResponse("Hola A-Nido app")

def colectivo(request):
	return render(request, "blog/integrantes.html", {})

def proyectos(request):
        return HttpResponse("Hola A-Nido app")

def piirspec(request):
        return render(request, "blog/proyecto.html")

def cam2019(request):
        return render(request, "blog/cam2019.html")

def craig(request):
        return render(request, "blog/entrevista_craig.html")

def cosito(request):
        return HttpResponse("Hola A-Nido app")

def contribuir(request):
        return render(request, "blog/contribuir.html")

def lecturas(request):
        return HttpResponse("Hola A-Nido app")

