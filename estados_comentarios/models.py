from django.db import models

class EstadoComentario(models.Model):
	nombre = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nombre
