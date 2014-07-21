from django.db import models

class HorarioProgramacion(models.Model):
	manana = models.TimeField()
	tarde_noche = models.TimeField()

	def __unicode__(self):
		return "Manana: " + str(self.manana) + " - Tarde/noche: " + str(self.tarde_noche)