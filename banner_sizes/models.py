from django.db import models

class BannerSize(models.Model):
	ancho = models.SmallIntegerField()
	alto = models.SmallIntegerField()	

	def __unicode__(self):
		return str(self.ancho) + "px * " + str(self.alto) + "px"