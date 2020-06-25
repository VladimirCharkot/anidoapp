from django.urls import path

from . import views

urlpatterns = [

    path('', views.index),

    path('nosotres/colectivo/', views.colectivo),
    path('nosotres/integrantes/', views.integrantes),
    path('nosotres/nido/', views.nido),

    path('proyectos/piirspec/', views.piirspec),
    path('proyectos/piirspec/cam2019/', views.cam19),
    path('proyectos/piirspec/craig/', views.craig),

    path('proyectos/cosito/', views.cosito),
    path('proyectos/cosito/itinerario/', views.itinerario),

    path('contribuir/', views.contribuir),

    path('lecturas/', views.lecturas),

#cam2019.html  contribuir.html  entrevista_craig.html  index.html  integrantes.html  proyecto.html
    # retro:
    path('cam2019.html', views.cam19),   # Pendiente: esta linea pincha
    path('contribuir.html', views.contribuir),
    path('entrevista_craig.html', views.craig),
    path('integrantes.html', views.colectivo),
    path('proyecto.html', views.piirspec),

    path('test/', views.test_articulo)
]
