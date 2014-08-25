from django.db import models
from entidades.models import Entidad 
from userprofiles.models import UserProfile
from formatChecker import ContentTypeRestrictedFileField

class Documento(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True)
	creado_para = models.ForeignKey(Entidad, default=1, blank=True, null=True)
	creado_por = models.ForeignKey(UserProfile,default=2)
	archivo = ContentTypeRestrictedFileField(upload_to='documents', content_types=['application/pdf', 'application/msword', ],max_upload_size=5242880)

	def __unicode__(self):
		return self.nombre