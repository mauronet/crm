from django.db import models
from respuestas_encuestas.models import RespuestaEncuesta

class Encuesta(models.Model):
	pregunta = models.CharField(max_length=255)
	activa = models.BooleanField()
	respuestas = models.ManyToManyField(RespuestaEncuesta)

	def __unicode__(self):
		return self.pregunta
