from django.db import models

from videos.models import Video

class Capitulo(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	direccion = models.TextField(blank=True)
	produccion = models.TextField(blank=True)
	duracion = models.CharField(max_length=255)
	video = models.ForeignKey(Video)

	def __unicode__(self):
		return self.nombre