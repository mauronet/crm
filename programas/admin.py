from django.contrib import admin

from .models import Programa

class ProgramaAdmin(admin.ModelAdmin):
	list_display = ('nombre','sinopsis','franja','produccion')
	list_filter = ('franja',)
	search_fields = ('nombre','sinopsis','detalles')
	filter_horizontal = ('capitulos','imagenes')

admin.site.register(Programa, ProgramaAdmin)