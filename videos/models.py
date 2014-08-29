from django.db import models

from tags.models import Tag
from franjas.models import Franja
from entidades.models import Entidad 
from categorias.models import Categoria
from django.core.validators import RegexValidator
from tipos_videos.models import TipoVideo 
from userprofiles.models import UserProfile

class Video(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	tipo = models.ForeignKey(TipoVideo, default=1)
	creado_para = models.ForeignKey(Entidad, default=1, blank=True, null=True, related_name='defaultEntidad')
	creado_por = models.ForeignKey(UserProfile,default=2)
	codigo = models.CharField(max_length=255)
	creditos =  models.TextField(blank=True)
	categorias = models.ManyToManyField(Categoria, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	franjas = models.ManyToManyField(Franja, blank=True)
	entidades = models.ManyToManyField(Entidad, blank=True)
	visto = models.SmallIntegerField(default=0)

	def img_thumbnail(self):
		return '<a href="https://www.youtube.com/watch?v=%s" target="_blank"><img src="http://img.youtube.com/vi/%s/0.jpg" height="100px"/></a>' % (self.codigo, self.codigo)
	img_thumbnail.allow_tags = True

	def __unicode__(self):
		return self.nombre