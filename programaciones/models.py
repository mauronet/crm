from django.db import models

from horarios_programacion.models import HorarioProgramacion
from franjas.models import Franja

class Programacion(models.Model):
	fecha = models.DateField()
	horario = models.ForeignKey(HorarioProgramacion)
	programa = models.TextField()
	franja = models.ForeignKey(Franja)
