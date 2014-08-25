from django.db import models

from noticias.models import Noticia

class NoticiasDestacadas(models.Model):
	noticias = models.ManyToManyField(Noticia, blank=True)