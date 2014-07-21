from django.db import models

from noticias.models import Noticia
from oportunidades.models import Oportunidad
from eventos.models import Evento
from entradas_blogs.models import EntradaBlog

class Carrusel(models.Model):
	noticias = models.ManyToManyField(Noticia, blank=True)
	oportunidades = models.ManyToManyField(Oportunidad, blank=True)
	eventos = models.ManyToManyField(Evento, blank=True)
	entradas = models.ManyToManyField(EntradaBlog, blank=True)
