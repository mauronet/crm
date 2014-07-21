from django.db import models

from estados_comentarios.models import EstadoComentario
from userprofiles.models import UserProfile

class Comentario(models.Model):
	usuario = models.ForeignKey(UserProfile)
	contenido = models.TextField();
	fecha = models.DateTimeField()
	estado = models.ForeignKey(EstadoComentario)

	def __unicode__(self):
		return "Comentario " + self.estado.nombre + " de " + self.usuario.user.username