from django.db import models

class TipoVideo(models.Model):
	nombre = models.CharField(max_length=255)
	extra = models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre