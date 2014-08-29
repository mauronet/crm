from django.db import models

class DocumentoEnLinea(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	url = models.URLField()

	def file_link(self):
		if self.url == "":
			return ''
		else:
			return '<a href="%s" target="_blank">%s</a>' % (self.url, self.url)
	file_link.allow_tags = True

	def __unicode__(self):
		return self.nombre