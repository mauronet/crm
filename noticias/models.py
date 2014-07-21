from django.db import models

from categorias.models import Categoria
from comentarios.models import Comentario
from entidades.models import Entidad 
from franjas.models import Franja
from imagenes.models import Imagen
from tags.models import Tag
from videos.models import Video
from documentos.models import Documento

class Noticia(models.Model):
	titulo = models.CharField(max_length=255)
	lead = models.TextField()
	contenido = models.TextField()
	fecha = models.DateField()
	direccion_web = models.URLField(blank=True)
	imagen_principal = models.ForeignKey(Imagen, related_name='imagenprincipal_noticias')
	
	categorias = models.ManyToManyField(Categoria, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	franjas = models.ManyToManyField(Franja, blank=True)
	entidades = models.ManyToManyField(Entidad, blank=True)
	imagenes_adicionales = models.ManyToManyField(Imagen, blank=True)
	videos = models.ManyToManyField(Video, blank=True)
	documentos = models.ManyToManyField(Documento, blank=True)
	comentarios = models.ManyToManyField(Comentario, blank=True)

	def __unicode__(self):
		return self.titulo;

	def get_absolute_url(self):
		return "/noticias/%s/" % (self.id)