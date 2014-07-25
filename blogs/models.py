from django.db import models

from entradas_blogs.models import EntradaBlog
from userprofiles.models import UserProfile
from entidades.models import Entidad

class Blog(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	administrador = models.ForeignKey(UserProfile,blank=True)
	entidad = models.ForeignKey(Entidad,blank=True, null=True)
	entradas = models.ManyToManyField(EntradaBlog, blank=True)

	def __unicode__(self):
		return self.nombre