from django.db import models

from tipos_entidades.models import TipoEntidad

class Entidad(models.Model):
	nombre = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255, blank=True)
	ciudad = models.CharField(max_length=255, blank=True)
	telefonos = models.CharField(max_length=255, blank=True)
	email = models.EmailField(blank=True)
	contacto = models.CharField(max_length=255, blank=True)
	logo = models.ImageField(upload_to="logos", blank=True)
	sitio_web = models.URLField(blank=True)
	tipo = models.ForeignKey(TipoEntidad)
	activo = models.BooleanField()
	latitud = models.FloatField(default=0)
	longitud = models.FloatField(default=0)

	def __unicode__(self):
		return self.nombre