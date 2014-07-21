from django.db import models
from entidades.models import Entidad 

class Documento(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	creado_por = models.ForeignKey(Entidad, default=1)
	archivo = models.FileField(upload_to="documents")

	def __unicode__(self):
		return self.nombre