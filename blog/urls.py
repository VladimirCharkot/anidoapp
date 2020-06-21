from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('colectivo/', views.colectivo),
    path('proyectos/', views.proyectos),
    path('proyectos/piirspec/', views.piirspec),
    path('proyectos/piirspec/cam2019/', views.cam2019),
    path('proyectos/piirspec/craig/', views.craig),
    path('proyectos/cosito/', views.cosito),
    path('contribuir/', views.contribuir),
    path('lecturas/', views.lecturas),

#cam2019.html  contribuir.html  entrevista_craig.html  index.html  integrantes.html  proyecto.html
    # retro:
    path('cam2019.html', views.cam2019),
    path('contribuir.html', views.contribuir),
    path('entrevista_craig.html', views.craig),
    path('integrantes.html', views.colectivo),
    path('proyecto.html', views.piirspec),
]
