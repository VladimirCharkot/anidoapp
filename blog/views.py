from django.shortcuts import render
from django.http import HttpResponse

# Markdown y custom
import markdown as md
from scripts.mdext.mdext import MDExt

from .articulos import *





def colectivo(request):
    return render(request, "blog/en_construccion.html")

def lecturas(request):
    return render(request, "blog/en_construccion.html")

def cosito(request):
    return render(request, "blog/en_construccion.html")

def nido(request):
    return render(request, "blog/en_construccion.html")

def itinerario(request):
    return render(request, "blog/en_construccion.html")



def index(request):
    return render(request, 'blog/pag.html', {'clase' : 'blog/index.html'})

def contribuir(request):
    return render_articulo(request, contrib)

def integrantes(request):
    return render_articulo(request, nosotrxs)


def cronica_1(request):
    return render_articulo(request, a_estudiar)

def piirspec(request):
    return render_articulo(request, proyecto)


def cam19(request):
    return render_articulo(request, cam2019)

def craig(request):
    return render_articulo(request, craig_entrevista)



#background-size: 200%;
#background-position: 20% 0%;

def render_articulo(request, articulo):
    contenido = open(articulo['contenido']['md'],'r',encoding='utf8').read()
    contenido_html = md.markdown(contenido, extensions=[MDExt(), 'extra', 'smarty'])
    articulo['contenido']['html'] = contenido_html
    return render(request, "blog/pag.html", context=articulo)

"""def test_articulo(request):
    articulo = nosotrxs
    contenido = open(articulo['contenido']['md'],'r',encoding='utf8').read()
    contenido_html = md.markdown(contenido, extensions=[MDExt(),'extra', 'smarty'])
    articulo['contenido']['html'] = contenido_html
    return render(request, "blog/pag.html", context=articulo)"""
