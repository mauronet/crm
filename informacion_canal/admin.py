from django.contrib import admin

from .models import InfoCanal

class InfoCanalAdmin(admin.ModelAdmin):
	list_display = ('id',)
	filter_horizontal = ('documentos','imagenes_adicionales_equipo_de_trabajo')

admin.site.register(InfoCanal, InfoCanalAdmin)