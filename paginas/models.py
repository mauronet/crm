from django.db import models

from banners_publicidad.models import BannerPublicidad

class Pagina(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	banner_superior = models.ForeignKey(BannerPublicidad, blank=True, related_name='banner1', null=True)
	banner_izquierdo = models.ForeignKey(BannerPublicidad, blank=True, related_name='banner2', null=True)
	banner_derecho = models.ForeignKey(BannerPublicidad, blank=True, related_name='banner3', null=True)
	banner_inferior = models.ForeignKey(BannerPublicidad, blank=True, related_name='banner4', null=True)
	
	def __unicode__(self):
		return self.nombre