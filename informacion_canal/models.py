from django.db import models
from documentos.models import Documento
from imagenes.models import Imagen

class InfoCanal(models.Model):
	acerca_de_zoom = models.TextField()
	equipo_de_trabajo = models.TextField()
	comite_de_programacion = models.TextField()
	comites_tecnicos_regionales = models.TextField()
	imagen_acerca_de_zoom = models.ImageField(upload_to="images_info_zoom", blank=True)
	imagen_equipo_de_trabajo = models.ImageField(upload_to="images_info_zoom", blank=True)
	imagenes_adicionales_equipo_de_trabajo = models.ManyToManyField(Imagen, blank=True)
	documentos = models.ManyToManyField(Documento, blank=True)