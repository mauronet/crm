from django.db import models

class RespuestaEncuesta(models.Model):
	respuesta = models.CharField(max_length=255)
	votos = models.SmallIntegerField(default=0)

	def __unicode__(self):
		return self.respuesta