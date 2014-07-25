from django.db import models
from entidades.models import Entidad
from userprofiles.models import UserProfile

class Imagen(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	creado_para = models.ForeignKey(Entidad, default=1, blank=True, null=True)
	creado_por = models.ForeignKey(UserProfile,default=2)
	creditos = models.TextField(blank=True)
	archivo = models.ImageField(upload_to="images")

	def __unicode__(self):
		return self.nombre