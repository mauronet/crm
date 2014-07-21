from django.db import models

from tags.models import Tag
from franjas.models import Franja
from entidades.models import Entidad 
from categorias.models import Categoria
from django.core.validators import RegexValidator
from tipos_videos.models import TipoVideo 

class Video(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	tipo = models.ForeignKey(TipoVideo, default=1)
	creado_por = models.ForeignKey(Entidad, default=1, related_name='defaultEntidad')
	codigo = models.CharField(max_length=255)
	creditos =  models.TextField(blank=True)
	categorias = models.ManyToManyField(Categoria, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	franjas = models.ManyToManyField(Franja, blank=True)
	entidades = models.ManyToManyField(Entidad, blank=True)

	def __unicode__(self):
		return self.nombre