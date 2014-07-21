from django.db import models

class TipoEntidad(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre
