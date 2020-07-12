from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import *

# Markdown y custom
import markdown as md
from scripts.mdext.mdext import MDExt

from .articulos import *


def en_construccion(request):
    return render(request, "blog/en_construccion.html")


# <!-- Portada -->

def index(request):
    skin = request.COOKIES.get('skin', 0)
    return render(request, 'blog/pag.html',
        {'clase' : 'blog/index.html', 'skin' : skin})


# <!-- Quienes somos -->

def proyectos(request):
    return render_articulo(request, los_proyectos)

def historia(request):
    return render_articulo(request, andado)

def nido(request):
    return render_articulo(request, nidito)

def integrantes(request):
    return render_articulo(request, nosotrxs)

def apoyo(request):
    return render_articulo(request, avales)




# <!-- Proyectos -->


def piirspec(request):
    return render_articulo(request, proyecto)

def cam19(request):
    return render_articulo(request, cam2019)

def craig(request):
    return render_articulo(request, craig_entrevista)


def cronica_1(request):
    return render_articulo(request, a_estudiar)


def salita(request):
    return render_articulo(request, sala)


def intervenciones(request):
    return render_articulo(request, interven)


# <!-- Contribuir -->

def contribuir(request):
    return render_articulo(request, contrib)










def serializar(articulo):
    art = {
        'clase'  : 'blog/articulo.html',
        'titulo' : articulo.titulo_pag,
        'contenido' : {
            'titulo' : articulo.titulo_articulo,
            'md' : articulo.contenido.archivo.path
        }
    }
    if articulo.img_titulo:
        art['contenido']['img_titulo'] = {
            'origen' : articulo.img_titulo.url(),
            'size' : articulo.img_titulo.size,
            'pos' : articulo.img_titulo.pos,
            'color' : articulo.img_titulo.color
        }

    if articulo.img_seccion:
        art['contenido']['img_seccion'] = {
            'origen' : articulo.img_seccion.url(),
            'size' : articulo.img_seccion.size,
            'pos' : articulo.img_seccion.pos,
            'color' : articulo.img_seccion.color
        }

    if articulo.img_menu:
        art['contenido']['img_menu'] = {
            'origen' : articulo.img_menu.url(),
            'size' : articulo.img_menu.size,
            'pos' : articulo.img_menu.pos,
            'color' : articulo.img_menu.color
        }

    if articulo.pdf:
        art['contenido']['pdf'] = {
            'link' : articulo.pdf.url(),
            'nombre' : articulo.pdf.nombre
        }

    if articulo.extras:
        art['contenido']['extras'] = [articulo.extras]

    if articulo.caratula:
        art['contenido']['caratula'] = articulo.caratula

    if articulo.intro:
        art['contenido']['intro'] = articulo.intro

    return art


def pagina(request, articulo):
    articulo_data = Articulo.objects.get(titulo_pag=articulo)
    js = serializar(articulo_data)
    return render_articulo(request, js)

    #return JsonResponse(data, safe=False)
    #return HttpResponse(data, content_type="application/json")


#background-size: 200%;
#background-position: 20% 0%;

def render_articulo(request, articulo):
    contenido = open(articulo['contenido']['md'],'r',encoding='utf8').read()
    contenido_html = md.markdown(contenido, extensions=[MDExt(), 'extra', 'smarty'])
    articulo['contenido']['html'] = contenido_html
    resp = render(request, "blog/pag.html", context=articulo)
    resp.set_cookie('skin', request.COOKIES.get('skin', 'luminoso'))
    return resp
