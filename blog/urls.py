from django.urls import path

from . import views

urlpatterns = [

    path('', views.index),

    path('nosotres/proyectos/', views.proyectos),
    path('nosotres/historia/', views.historia),
    path('nosotres/nido/', views.nido),
    path('nosotres/integrantes/', views.integrantes),
    path('nosotres/apoyo/', views.apoyo),

    path('piirspec/', views.piirspec),
    path('piirspec/cam2019/', views.cam19),
    path('piirspec/craig/', views.craig),
    path('piirspec/arena/', views.arena),
    path('piirspec/cam22/', views.cam22),

    path('cronicas/1/', views.cronica_1),

    path('salita/', views.salita),

    path('intervenciones/', views.intervenciones),

    path('contribuir/', views.contribuir),

    path('biblioteca/cirqueros/', views.cirqueros),



#_cam2019.html  _contribuir.html  _entrevista_craig.html  _index.html  _integrantes.html  _proyecto.html
    # retro:
    # path('cam2019.html', views.cam19),
    # path('contribuir.html', views.contribuir),
    # path('entrevista_craig.html', views.craig),
    # path('integrantes.html', views.integrantes),
    # path('proyecto.html', views.piirspec),

    path('test/', views.pagina, {'articulo': 'CAM 2019'})
]


# HOLA JERE
