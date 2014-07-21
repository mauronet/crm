from django.db import models

from franjas.models import Franja
from videos.models import Video
from capitulos.models import Capitulo
from imagenes.models import Imagen
from entidades.models import Entidad

class Programa(models.Model):
	nombre = models.CharField(max_length=255)
	franja = models.ForeignKey(Franja)
	entidad = models.ForeignKey(Entidad, null=True, blank=True)
	produccion = models.BooleanField()
	sinopsis = models.TextField(blank=True)
	video = models.ForeignKey(Video, null=True, blank=True)
	banner = models.ImageField(upload_to="banners", blank=True) 
	color_fondo = models.CharField(max_length=6, blank=True)
	color_linea = models.CharField(max_length=6, blank=True)
	color_letra = models.CharField(max_length=6, blank=True)
	tipo_letra = models.CharField(max_length=30, blank=True)
	capitulos = models.ManyToManyField(Capitulo, blank=True)
	imagenes = models.ManyToManyField(Imagen, blank=True)

	def __unicode__(self):
		return self.nombre

#cambiar imagen a objeto Imagen