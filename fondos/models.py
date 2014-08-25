from django.db import models

class Fondo(models.Model):
	nombre = models.CharField(max_length=255)
	archivo = models.ImageField(upload_to="fondos")

	def __unicode__(self):
		return self.nombre