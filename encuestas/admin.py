from django.contrib import admin

from .models import Encuesta

class EncuestaAdmin(admin.ModelAdmin):
	list_display = ('pregunta', 'activa')
	filter_horizontal = ('respuestas',)

admin.site.register(Encuesta, EncuestaAdmin)