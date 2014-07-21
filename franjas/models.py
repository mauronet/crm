from django.db import models

class Franja(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	color = models.CharField(max_length=6, blank=True)
	imagen = models.ImageField(upload_to="images", blank=True)
	codigo_html_video = models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre