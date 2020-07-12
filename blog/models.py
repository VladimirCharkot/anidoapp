# -*- coding: utf-8 -*-
from django.db import models


class ArchivoImagen(models.Model):
    etiqueta = models.CharField(
        max_length=80, help_text="Etiqueta para identificar el *contenido* de la imagen")
    origen = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.etiqueta


class Imagen(models.Model):
    etiqueta = models.CharField(
        max_length=80, help_text="Etiqueta para identificar *lugar* (rol/posición/etc) que va a ocupar este archivo posicionado y filtrado con estos valores css")
    archivo = models.ForeignKey(ArchivoImagen,
                                on_delete=models.CASCADE)
    size = models.CharField('Tamaño (css)',
                            max_length=20,
                            default='cover')
    pos = models.CharField('Posición (css)',
                           max_length=20,
                           default='center')
    color = models.CharField('Color (css)',
                             max_length=20,
                             default='#fff')
    blend_mode = models.CharField('Blend mode (css)',
                                  max_length=20,
                                  default='color-dodge')

    def url(self):
        return self.archivo.origen.url

    def __str__(self):
        return self.etiqueta


class PDF(models.Model):
    archivo = models.FileField(upload_to='pdf/')
    nombre = models.CharField(max_length=200)

    def get_nombre(self):
        return self.nombre if self.nombre.endswith('.pdf') else self.nombre + '.pdf'

    def url(self):
        return self.archivo.url

    def __str__(self):
        return self.nombre


class MD(models.Model):
    archivo = models.FileField(upload_to='md/')
    nombre = models.CharField(max_length=200)

    def url(self):
        return self.archivo.url

    def get_nombre(self):
        return self.nombre if self.nombre.endswith('.md') else self.nombre + '.md'

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    #clase = models.CharField(max_length=80)

    titulo_pag = models.CharField(max_length=80,
                                  help_text="Título que aparece en la pestaña.")

    titulo_articulo = models.CharField(max_length=200,
                                       help_text="Título que aparece en la cabeza del artículo.")

    img_titulo = models.ForeignKey(Imagen, on_delete=models.CASCADE, related_name="img_cabecera",
                                   help_text="Imagen de fondo para la cabeza del artículo.")

    img_seccion = models.ForeignKey(Imagen,
                                    on_delete=models.CASCADE,
                                    related_name="img_seccion",
                                    help_text="Imagen de fondo para los subtítulos del artículo.")

    pdf = models.ForeignKey(PDF,
                            blank=True,
                            on_delete=models.CASCADE,
                            help_text="PDF para descarga")

    intro = models.TextField(max_length=1500,
                             help_text="Texto entre cabeza y cuerpo del artículo.")

    caratula = models.CharField(max_length=80,
                                blank=False,
                                help_text="Carátula, opcional. Indicar archivo html.")

    contenido = models.ForeignKey(MD,
                                  blank=True,
                                  on_delete=models.CASCADE,
                                  help_text="Contenido del artículo, en formato markdown (.md)")

    extras = models.TextField(
        max_length=80, help_text="Extras al final, opcional. Indicar archivos html.")

    def get_extras(self):
        return self.extras.split('\n')

    img_menu = models.ForeignKey(Imagen, on_delete=models.CASCADE)
    pie_menu = models.CharField(max_length=200,
                                help_text="Pie de foto en el menú")

    def __str__(self):
        return self.titulo_pag
