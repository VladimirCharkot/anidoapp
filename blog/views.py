from django.shortcuts import render
from django.http import HttpResponse

# Markdown y custom
import markdown as md
from scripts.mdext.mdext import MDExt

def index(request):
    return render(request, 'blog/index.html', {})
#	return HttpResponse("Hola A-Nido app")

def colectivo(request):
    return render(request, "blog/integrantes.html", {})

def piirspec(request):
    return render(request, "blog/proyecto.html", {})

def cam19(request):
    return render(request, "blog/cam2019.html", {})

def craig(request):
    return render(request, "blog/entrevista_craig.html")

def contribuir(request):
    return render(request, "blog/contribuir.html")



def lecturas(request):
    return render(request, "blog/en_construccion.html")

def cosito(request):
    return render(request, "blog/en_construccion.html")

def integrantes(request):
    return render(request, "blog/en_construccion.html")

def nido(request):
    return render(request, "blog/en_construccion.html")

def itinerario(request):
    return render(request, "blog/en_construccion.html")


cam2019 = {
    'clase' : 'blog/articulo.html',
    'titulo': 'CAM 2019',

    'extras': ['blog/cam2019/biblio.html'],

    'contenido' : {
        'titulo': 'Re.flexionando sobre las prácticas docentes en las artes circenses contemporáneas.',
        'imagen_titulo': 'fotos/cam_3.jpg',
        'pdf' : {
            'link' : '/static/blog/cam_2019.pdf',
            'nombre' : 'Proyecto A-Nido - Análisis CAM 2019.pdf'
        },
        'caratula' : 'blog/cam2019/caratula_analisis_cam.html',
        'intro': 'Algunos aportes desde lo trabajado en la Convención de Malabares 2019. San Francisco, Córdoba – Argentina.',
        'md' : 'blog/static/blog/textos/cam2019.md'
    }
}

sala_cosito = {
    'clase' : 'blog/articulo.html',
    'titulo': 'C O S I T O',

    'contenido' : {
        'titulo': 'Una <span style="font-size: 1.6em;">pequeña</span> sala de lectura itinerante para <span style="font-size: 0.7em;">grandes</span> exploradores.',
        'subtitulo': '',
        'imagen_titulo': 'fotos/libros.jpg',
        'md' : 'blog/static/blog/textos/cosito.md'
    }
}


def test_articulo(request):
    articulo = cam2019
    contenido = open(articulo['contenido']['md'],'r',encoding='utf8').read()
    contenido_html = md.markdown(contenido, extensions=[MDExt(),'extra', 'smarty'])
    articulo['contenido']['html'] = contenido_html
    return render(request, "blog/pag.html", context=articulo)
