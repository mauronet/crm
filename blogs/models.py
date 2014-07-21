from django.db import models

from entradas_blogs.models import EntradaBlog
from userprofiles.models import UserProfile
from entidades.models import Entidad

class Blog(models.Model):
	nombre = models.CharField(max_length=255)
	entidad = models.ForeignKey(Entidad,blank=True)
	entradas = models.ManyToManyField(EntradaBlog, blank=True)

	def __unicode__(self):
		return self.nombre