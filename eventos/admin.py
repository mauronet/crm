from django.contrib import admin

from .models import Evento

class EventoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'lugar')
	search_fields = ('nombre', 'descripcion', 'lugar')
	filter_horizontal = ('comentarios','categorias','tags','franjas','entidades','imagenes_adicionales','videos','documentos')

admin.site.register(Evento, EventoAdmin)
