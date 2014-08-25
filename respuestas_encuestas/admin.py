from django.contrib import admin

from .models import RespuestaEncuesta

class RespuestaEncuestaAdmin(admin.ModelAdmin):
	list_display = ('respuesta', 'votos')

admin.site.register(RespuestaEncuesta, RespuestaEncuestaAdmin)