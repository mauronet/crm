from django.db import models

class DocumentoEnLinea(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	url = models.URLField()

	def __unicode__(self):
		return self.nombre