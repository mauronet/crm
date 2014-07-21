from django.db import models
from entidades.models import Entidad

class Imagen(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	creado_por = models.ForeignKey(Entidad, default=1)
	creditos = models.TextField(blank=True)
	archivo = models.ImageField(upload_to="images")

	def __unicode__(self):
		return self.nombre