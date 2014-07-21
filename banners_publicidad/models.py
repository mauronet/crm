from django.db import models
from banner_sizes.models import BannerSize

class BannerPublicidad(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	tamano = models.ForeignKey(BannerSize)
	imagen = models.ImageField(upload_to="banners", blank=True)
	direccion_web = models.URLField(blank=True)
	codigo_html = models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre + '(' + str(self.tamano.ancho) + 'px * ' + str(self.tamano.alto) + 'px)'