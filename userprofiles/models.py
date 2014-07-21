from django.db import models
from django.contrib.auth.models import User

from tipos_usuario.models import TipoUsuario
from entidades.models import Entidad

class UserProfile(models.Model):
	GENEROS = (
		('M', 'Masculino'),
		('F', 'Femenino'),
    )
	user = models.OneToOneField(User)
	tipo = models.ForeignKey(TipoUsuario)
	entidad = models.ForeignKey(Entidad, blank=True, null=True)
	avatar = models.ImageField(upload_to="avatars", blank=True)
	biografia = models.TextField(blank=True)
	ciudad = models.CharField(max_length=255, blank=True)
	fecha_nacimiento = models.DateField(null=True,blank=True)
	sexo =  models.CharField(max_length=1, blank=True, choices=GENEROS)
	activation_key = models.CharField(max_length=40, blank=True)
	anotaciones_internas = models.TextField(blank=True)
	def __unicode__(self):
		return self.user.username