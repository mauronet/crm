from django.db import models
import datetime

class Suscriptor(models.Model):
	email = models.EmailField(max_length=70, unique=True)
	now = datetime.datetime.now()
	fecha_suscripcion = models.DateTimeField(default=now)

	def __unicode__(self):
		return self.email